from django.shortcuts import render
from .forms import ToppingForm, PizzaForm, OrderForm
from .models import Topping, Pizza, Order

def home(request):
	template_name = 'website/home_view.html'
	context = {}
	return render(request, template_name, context=context)

def order(request):
	form = OrderForm()
	template_name = 'website/order_form.html'
	return render(request, template_name, {'form':form})

def pizza(request):
	# if request.method == 'POST':
	# 	form = PizzaForm(request.POST)
	# 	if form.is_valid():
	# 		data = form.cleaned_data
	# 		pizza_name = data.get('pizza_name')
	# 		size = data.get('size')
	# 		toppings = data.get('toppings')
	# 		price_pizza = data.get('price_pizza')
	# 		db_register = Pizza(
	# 			pizza_name = pizza_name,
	# 			size = size,
	# 			toppings = toppings,
	# 			price_pizza = price_pizza
	# 		)
	# 		db_register.save()
	# else:
	form = PizzaForm()
	template_name = 'website/pizza_form.html'
	return render(request, template_name, {'form':form})

def topping(request):
	if request.method == 'POST':
		form = ToppingForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			topping_name = data.get('topping_name')
			calories = data.get('calories')
			unit = data.get('unit')
			price_topping = data.get('price_topping')
			db_register = Topping(
				topping_name = topping_name,
				calories = calories,
				unit = unit,
				price_topping = price_topping
			)
			db_register.save()
	else:
		form = ToppingForm()
	template_name = 'website/topping_form.html'
	return render(request, template_name, {'form':form})