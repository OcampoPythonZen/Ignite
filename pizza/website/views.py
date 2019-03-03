from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from website import models

# Create your views here.
class HomeView(TemplateView):
    template_name = 'website/home_view.html'

class NewOrderView(CreateView):
	model = models.Order
	fields = ('pizzas','is_finished')