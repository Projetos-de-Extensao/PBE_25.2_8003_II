"""
URL configuration for monitoria project.
"""
from django.contrib import admin
from django.urls import path, include  # <-- Adicione 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vagas.urls')),  # <-- Adicione esta linha
]