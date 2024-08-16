from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_image')

    

        
    def get_url(self):
        return reverse('product_by_category', args=[self.slug])
    def __str__(self) -> str:
        return self.category_name