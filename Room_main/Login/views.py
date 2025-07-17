from django.shortcuts import render



def login_here(request):
    return render(request, 'login.html')
