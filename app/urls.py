
from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name= 'home'),
    path('Todos/', Todo_list, name='Todo_list'),
   
    
    
]
