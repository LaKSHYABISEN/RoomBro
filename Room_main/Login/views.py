from django.shortcuts import render

# Create your views here.

def login_here(request):
    return render(request, 'login.html')
