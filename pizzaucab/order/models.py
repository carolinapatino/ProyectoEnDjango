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
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


class Order(models.Model):
    date = models.DateField()
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)





    
