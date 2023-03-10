from django.urls import path, include
from .views import *

urlpatterns = [
    path('', news_home, name='news_home'),
    path('add/', news_adder, name='news_add'),
    path('filter', filter, name='filter'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='news_delete'),
]