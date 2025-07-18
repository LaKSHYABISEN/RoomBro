from django.urls import path
from . import views
from Home.views import home_view

urlpatterns = [
    path('', views.login_here, name="login_here"),
    path('home/', home_view, name="Home_Page"),
]
