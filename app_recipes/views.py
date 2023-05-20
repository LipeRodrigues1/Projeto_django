from django.shortcuts import render
from django.http import HttpResponse


def my_home(request):
    return render(request, 'home.html', context={
        'name': 'Fellipe Augusto'
    })


def sobre(resquest):
    return HttpResponse('Essa pagina é o SOBRE')


def contato(request):
    return HttpResponse('(81) 996018125')


# Create your views here.
