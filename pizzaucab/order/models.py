from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    ci = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.lastname

class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)





    
