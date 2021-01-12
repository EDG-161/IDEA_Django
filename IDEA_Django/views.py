from django.shortcuts import render
from django.template import loader


def home(request):
    returned = "Hola"
    template = loader.get_template('templates/home.html')
    return render(request, 'templates/home.html', {'returned': returned})
