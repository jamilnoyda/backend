# Create your models here.
from __future__ import unicode_literals
from django.db import models


from django.utils import timezone
from django.db import transaction

from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from users.managers import UserManager
 
class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User.
    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
 
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self