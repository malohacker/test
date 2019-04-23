from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    subscription = models.BooleanField('Подписка', default=False)
