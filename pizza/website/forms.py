from django import forms
from .models import Order,Pizza,Topping

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = '__all__'
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'