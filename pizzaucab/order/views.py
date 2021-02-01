from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Order, Size, Pizza, Ingredient

# Create your views here.
def index(request):
    ingredients = Ingredient.objects.all()
    sizes = Size.objects.all()
    context = {
        'ingredients': ingredients,
        'sizes': sizes,       
    }
    return render(request,'order/index.html', context)

def detail(request, order_id):
    return HttpResponse("Esta buscando la pizza %s" % order_id)

