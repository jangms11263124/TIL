from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    interest_stocks = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)