from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_image')

    

        
    def get_url(self):
        return reverse('product_by_category', args=[self.slug])
    def __str__(self) -> str:
        return self.category_name