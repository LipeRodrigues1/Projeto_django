from django.shortcuts import render
from django.http import HttpResponse


def my_home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Fellipe Augusto'
    })


def sobre(resquest):
    return HttpResponse('Essa pagina é o SOBRE')


def contato(request):
    return render(request, 'recipes/contato.html')


# Create your views here.
