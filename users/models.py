from django.contrib.auth.models import AbstractUser, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('superuser', 'Superuser'),
        ('moderator', 'Moderator'),
        ('employee', 'Employee'),
    )
    user_role = models.CharField(max_length=20, choices=USER_ROLES, default='employee')
    is_superuser = models.BooleanField(default=False)

    class Meta:
        # Add this to avoid clashing with the default User model
        swappable = 'AUTH_USER_MODEL'


    def __str__(self):  
        return f'{self.username} - {self.user_role}'

class UserRolePermission(models.Model):
    user_role = models.CharField(max_length=20, choices=CustomUser.USER_ROLES)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user_role', 'permission']]
