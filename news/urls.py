from django.urls import path, include
from .views import *

urlpatterns = [
    path('', news_home, name='news_home'),
    path('add/', news_adder, name='news_add'),
]