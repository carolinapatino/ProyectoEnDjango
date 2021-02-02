from django.forms import ModelForm
from .models import Pizza
from django import forms


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = [
            'size',
            'ingredient'
        ]

        labels = {
            'size': 'Tamaño',
            'ingredient': 'Ingredientes'
        }

        widgets = {
            'size': forms.Select(attrs={'class':'form-control'}),
            'ingredient': forms.CheckboxSelectMultiple()
        }