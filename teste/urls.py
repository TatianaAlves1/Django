from unicodedata import name
from django.urls import path, include
from teste.views import *

urlpatterns = [
    path('',home,name='home'),
    path('form/',calcular,name='calcular')
]