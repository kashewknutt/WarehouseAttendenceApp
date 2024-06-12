from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('superuser', 'Superuser'),
        ('moderator', 'Moderator'),
        ('employee', 'Employee'),
    )
    user_role = models.CharField(max_length=20, choices=USER_ROLES, default='employee')

    class Meta:
        # Add this to avoid clashing with the default User model
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return f'{self.username} - {self.user_role}'

# Add unique related_name arguments for groups and user_permissions
CustomUser.groups.field.related_name = 'customuser_groups'
CustomUser.user_permissions.field.related_name = 'customuser_user_permissions'
