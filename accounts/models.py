from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils import Choices
from django.conf import settings


class CustomUser(AbstractUser):

    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=1, choices=settings.USER_ROLE_TYPE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.email
