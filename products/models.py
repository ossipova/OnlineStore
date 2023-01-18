from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    currency = models.CharField(max_length=3, null=True)
    rate = models.FloatField()


class Review(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
