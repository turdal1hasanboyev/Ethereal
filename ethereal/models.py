from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    image = models.ImageField(upload_to='accounts_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.get_full_name():
            return f'{self.get_full_name()}'
        
        return f'{self.username}'


class Ethereal(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Work(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to='work_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    


class Testimonial(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, null=True, blank=True, related_name='testimonial_user')
    testimonial = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'


class About(models.Model):
    bio = models.TextField(null=True, blank=True)
    bio_2 = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'


class Contact(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
