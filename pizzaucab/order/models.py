from django.db import models

# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    
class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class Order(models.Model):
    date = models.DateField()
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)





    
