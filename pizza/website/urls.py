from django.urls import path, include
from website.views import home, order

urlpatterns = [
    path('',home),
    path('new/',order),
]