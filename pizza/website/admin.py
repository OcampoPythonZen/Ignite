from django.contrib import admin
from .models import Calorie,Ingredient,Pizza #Testing the models with the django-admin. thus i imported them.

# Register your models here.
admin.site.register(Calorie)
admin.site.register(Ingredient)
admin.site.register(Pizza)