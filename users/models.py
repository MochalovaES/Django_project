from django.db import models
from django.contrib.auth.models import AbstractUser

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    email_verify = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


