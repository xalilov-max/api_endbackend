# account/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  
    is_instructor = models.BooleanField(default=False)  # O'qituvchi yoki foydalanuvchi

    def __str__(self):
        return self.username  # Foydalanuvchining username'ini qaytaradi

