from django.db import models

# Create your models here.


class stores(models.Model):
    store_id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    