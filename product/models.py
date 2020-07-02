from django.db import models


# Create your models here.


class Products(models.Model):
    


class Food(Products):
    category = models.CharField(max_length=100)
