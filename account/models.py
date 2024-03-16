from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    avatar = models.CharField(max_length=40 , verbose_name="تصویر کاربر")
    email_active = models.CharField(max_length=94 , verbose_name="کد فعال ساز ایمیل")
