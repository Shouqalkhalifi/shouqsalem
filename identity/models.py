from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    full_name = models.CharField(max_length=150, verbose_name="الاسم الكامل")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الجوال")

    def __str__(self):
        return self.username
