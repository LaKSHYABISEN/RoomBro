
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_here, name="login_here"),
    
]