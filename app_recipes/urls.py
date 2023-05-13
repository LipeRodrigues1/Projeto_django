from django.urls import path
from app_recipes.views import my_home, sobre, contato


urlpatterns = [
    path('', my_home),
    path('sobre/', sobre),  # dominio.com/sobre/
    path('contato/', contato),  # dominio.com/contato/
]
