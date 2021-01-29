from django.contrib import admin
from .models import Size, Ingredient, Pizza, Order

admin.site.register(Size)
admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Order)