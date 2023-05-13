from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),  # dominio.com/admin
    path('', include('app_recipes.urls')),  # dominio.com
]