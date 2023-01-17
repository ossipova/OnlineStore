from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=6)
    review = models.TextField(blank=True, null=True)
    rate = models.FloatField()
