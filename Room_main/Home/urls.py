from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name="Home_Page"),
    
]