from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def my_view(request):
    return HttpResponse('Uma pagina sobre view')


def void(request):
    return HttpResponse('Essa é a pagina inicial')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('view/', my_view),
    path('', void),
        
]
