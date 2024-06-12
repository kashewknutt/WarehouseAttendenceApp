# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('superuser', 'Superuser'),
        ('moderator', 'Moderator'),
        ('employee', 'Employee'),
    )
    user_role = models.CharField(max_length=20, choices=USER_ROLES, default='employee')

    def __str__(self):
        return f'{self.username} - {self.user_role}'
