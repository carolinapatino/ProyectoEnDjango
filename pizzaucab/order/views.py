from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Order, Size, Pizza, Ingredient
from .forms import PizzaForm, OrderForm

# Create your views here.
def index(request):
    ingredients = Ingredient.objects.all()
    sizes = Size.objects.all()
    pizzas = Pizza.objects.all()
    form = OrderForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = OrderForm(request.POST)
        # Si el formulario es válido...

        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            # instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            form.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/order/addPizza')
    else:
        form = OrderForm()

    # Si llegamos al final renderizamos el formulario
    return render(request, "order/home.html", {'form': form, 'ingredients': ingredients, 'sizes': sizes, 'pizzas': pizzas })


def orderDetail(request):
    ingredients = Ingredient.objects.all()
    sizes = Size.objects.all()
    pizzas = Pizza.objects.all()
    context = {
        'ingredients': ingredients,
        'sizes': sizes,      
        'pizzas': pizzas 
    }
    return render(request,'order/orderDetail.html', context)

def detail(request, order_id):
    return HttpResponse("Esta buscando la pizza %s" % order_id)

def addPizza(request):
    # Creamos un formulario vacío
    ingredients = Ingredient.objects.all()
    sizes = Size.objects.all()
    pizzas = Pizza.objects.all()
    # order_id = order_id
    form = PizzaForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        
        form = PizzaForm(request.POST, initial={'order': "Antonio"})
        # Si el formulario es válido...

        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            # instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
           
            form.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/order/addPizza')
    else:
        form = PizzaForm()

    # Si llegamos al final renderizamos el formulario
    return render(request, "order/index.html", {'form': form, 'ingredients': ingredients, 'sizes': sizes, 'pizzas': pizzas})

def addOrder(request):
    # Creamos un formulario vacío
    ingredients = Ingredient.objects.all()
    sizes = Size.objects.all()
    pizzas = Pizza.objects.all()
    form = OrderForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = PizzaForm(request.POST)
        # Si el formulario es válido...

        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            # instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
           
            form.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/order')
    else:
        form = PizzaForm()

    # Si llegamos al final renderizamos el formulario
     
    return render(request, "order/index.html", {'form': form, 'ingredients': ingredients, 'sizes': sizes, 'pizzas': pizzas })

def deletePizza(request, id):
    pizza = Pizza.objects.get(id=id)
    try:
        pizza.delete()
    except:
        pass
    return redirect('order/addPizza')

def Reports (request):
    return render(request, "order/reports.html")

def orders (request):
    orders = Pizza.objects.all()
    return render(request, "order/orders.html", {'orders': orders, 'title': 'Ventas Realizadas'})

def ordersBySize (request, size):
    orders = Pizza.objects.filter(size__name=size)
    return render(request, "order/orders.html", {'orders': orders, 'title': 'Ventas Realizadas por tamaño'})

def ordersByIngredient (request, ingredient):
    orders = Pizza.objects.filter(ingredient__name=ingredient)
    return render(request, "order/orders.html", {'orders': orders, 'title': 'Ventas Realizadas por ingrediente'})

def ordersByClient (request, client):
    orders = Pizza.objects.filter(order__name=client)
    return render(request, "order/orders.html", {'orders': orders, 'title': 'Ventas Realizadas por cliente'})