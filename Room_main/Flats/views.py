from django.shortcuts import render

# Create your views here.
def flats_1bhk(request):
    return render(request, 'bhk_1.html')

def flats_2bhk(request):
    return render(request, 'bhk_2.html')

def flats_3bhk(request):
    return render(request, 'bhk_3.html')

def flats_4bhk(request):
    return render(request, 'bhk_4.html')
