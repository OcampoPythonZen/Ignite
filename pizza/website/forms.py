from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('size','toppings')
        widget = {
            'size' : forms.RadioSelect(),
            'toppings' : forms.CheckboxSelectMultiple()
        }