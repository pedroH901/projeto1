# recipes/urls.py
from django.urls import path
from . import views

path('', views.home, name='recipes_home'),

urlpatterns = [
path('', views.home, name='recipes_home'),
]