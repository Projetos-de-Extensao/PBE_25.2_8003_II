"""
URL configuration for monitoria project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # <-- IMPORTE ISTO

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vagas.urls')),
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'), # <-- ADICIONE ESTA LINHA
]