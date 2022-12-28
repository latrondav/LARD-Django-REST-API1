from django.urls import path
from . import views

urlpatterns = [
    path('', views.drink_list)
    #path('drinks/', views.drink_list)
]