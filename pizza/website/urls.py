from django.urls import (path, include)
from .views import HomeView
from website.views import NewOrderView

urlpatterns = [
    path('',HomeView.as_view()),
    path('new/',NewOrderView.as_view(),name='Nueva Orden')
]