from django.urls import path, include
from website.views import home, order, pizza, topping

urlpatterns = [
    path('',home),
    path('new/',order, name='orden'),
    path('pizza/',pizza,name='pizza'),
    path('topping/',topping,name='topping'),
]