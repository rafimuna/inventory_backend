from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_employee = models.BooleanField(default=False)

    # Solve group & permission reverse accessor clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',   # default 'user_set' clash হলে পরিবর্তন
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # default clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
