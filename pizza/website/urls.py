from django.urls import path, include
from website.views import home, order, pizza, topping

urlpatterns = [
    path('',home),
    path('new/',order),
    path('pizza/',pizza),
    path('topping/',topping),
]