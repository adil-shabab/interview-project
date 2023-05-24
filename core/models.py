from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='products')
    description = models.TextField()