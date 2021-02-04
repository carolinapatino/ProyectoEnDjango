from django.forms import ModelForm
from .models import Pizza, Ingredient, Order
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name',
            'lastname',
            'ci',
            'city'
        ]

        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'ci': 'Cédula de identidad',
            'city': 'Ciudad'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'ci': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
        }


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = [
            'size',
            'ingredient',
            'order'
        ]

        labels = {
            'size': 'Tamaño',
            'ingredient': 'Ingredientes',
            'order': 'Orden'
        }

        widgets = {
            'size': forms.Select(attrs={'class':'form-control'}),
            'ingredient': forms.CheckboxSelectMultiple(),
            'order': forms.Select(attrs={'class':'form-control'})
        }
