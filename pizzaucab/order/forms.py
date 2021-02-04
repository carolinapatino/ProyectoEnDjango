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

    def __init__(self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)
        self.fields['order'].initial = Order.objects.latest('id')
        self.fields['total'].initial = 0

    class Meta:
        model = Pizza
        fields = [
            'order',
            'size',
            'ingredient',
            'total'
        ]

        labels = {
            'order': 'Orden Número:',
            'size': 'Tamaño',
            'ingredient': 'Ingredientes',
            'total':'Su total'
        }

        widgets = {
            'order': forms.TextInput(attrs={'class':'form-control'}),
            'size': forms.Select(attrs={'class':'form-control'}),
            'ingredient': forms.CheckboxSelectMultiple() ,
            'total': forms.TextInput(attrs={'class':'form-control'})
        }

    def save (self, *args, **kwargs):
        super().save(*args, **kwargs)

