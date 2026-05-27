from django.db import models
# from django.contrib.auth import models as auth_models

from django.contrib.auth.models import AbstractUser

# Create your models here.
# 장고에서 주는 유저를 쓸거라서... 라이브러리 가져와야함!! 
class User(AbstractUser):
    pass