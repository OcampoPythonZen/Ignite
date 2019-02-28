from django.contrib import admin
from .models import Pizza,Topping,Size,Customer
#Testing the models with the django-admin. thus i imported them.

# Register your models here.
admin.site.register(Customer)
admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Pizza)