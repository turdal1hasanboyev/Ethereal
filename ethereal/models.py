from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    image = models.ImageField(upload_to='accounts_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
