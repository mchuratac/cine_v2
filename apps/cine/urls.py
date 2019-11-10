from django.urls import path
from .views import ListarLocales, CrearLocal
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar_locales/', login_required(ListarLocales.as_view()), name='listar_locales'),
    path('crear_local/', CrearLocal.as_view(), name='crear_local'),    
]