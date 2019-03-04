from django.shortcuts import render
from .forms import ToppingForm, PizzaForm, OrderForm

def home(request):
	template_name = 'website/home_view.html'
	context = {}
	return render(request, template_name, context=context)

def order(request):
	form = OrderForm()
	template_name = 'website/order_form.html'
	return render(request, template_name, {'form':form})

def pizza(request):
	form = PizzaForm()
	template_name = 'website/pizza_form.html'
	return render(request, template_name, {'form':form})

def topping(request):
	form = ToppingForm()
	template_name = 'website/topping_form.html'
	return render(request, template_name, {'form':form})