from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Product')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Picture(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m', default='images/default.png', max_length=200)
    product_of = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Images', default=None)

    def __str__(self):
        return self.name