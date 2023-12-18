from django.contrib import admin
from django.urls import path, include
from .views import DetalharCarrosView, ListaCarrosView, CriarCarrosView


urlpatterns = [
    path('', ListaCarrosView.as_view(), name='listar-carro'),
    path('cadastrar/', CriarCarrosView.as_view(), name='cadastrar-carro'),
    path('<int:pk>', DetalharCarrosView.as_view(), name='detalhar-carro'),
   ] 