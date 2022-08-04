from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager

# Create your models here

class Todolists(models.Model):
    username = models.CharField(max_length=64, default='')
    firstname = models.CharField(max_length=64, default='')
    lastname = models.CharField(max_length=64, default='')
    # email = models.CharField(max_length=64)
    email = models.EmailField(_('email address'), unique=True)
    # email = models.EmailField(max_length=70, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
