from django.contrib.auth.models import AbstractUser
from django.db import models

from COAX_test import settings


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    price = models.IntegerField()


class Order(models.Model):
    name = models.CharField(max_length=65)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
