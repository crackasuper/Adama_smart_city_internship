from django.db import models
from django.utils import timezone

# Create your models here.


class stores(models.Model):
    store_id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100)
    quantity = models.BigIntegerField()
    price = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.product}'

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self) -> str:
        return f'{self.product_name}'

class Dashboard(models.Model):
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_products = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_customers = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Total sales :  {self.total_sales}'
    
    top_selling_products = models.CharField(max_length=255, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f'Dashboard for {self.date}'
    
