from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_flats, name='flats'),
    path('1bhk/', views.flats_1bhk, name='flat_1bhk'),
    path('2bhk/', views.flats_2bhk, name='flat_2bhk'),
    path('3bhk/', views.flats_3bhk, name='flat_3bhk'),
    path('4bhk/', views.flats_4bhk, name='flat_4bhk'),
]