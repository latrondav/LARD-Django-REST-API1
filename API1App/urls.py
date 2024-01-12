from django.urls import path
from . import views

urlpatterns = [
    path('getallmanufacturers/', views.GetAllManufacturers),
    path('postmanufacturer/', views.PostManufacturers),
    path('deletemanufacturer/<int:id>/', views.DeleteManufacturer)
]