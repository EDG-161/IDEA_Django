#from . import logic
from django.shortcuts import render


# Create your views here.  ta weno pues

def home(request):   
    
    return render(request, 'plano.html')

def cifrar(request):   

    return render(request, 'cifrar.html')

def descifrar(request):  

    return render(request, 'descifrar.html')
