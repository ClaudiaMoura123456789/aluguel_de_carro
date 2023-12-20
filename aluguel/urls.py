from django.contrib import admin
from django.urls import path, include
from .views import DetalharCarrosView, ListaCarrosView, CriarCarrosView, AtualizarCarrosView, DeletarCarrosView, CriarAluguelView


urlpatterns = [
    path('', ListaCarrosView.as_view(), name='listar-carro'),
    path('cadastrar/', CriarCarrosView.as_view(), name='cadastrar-carro'),
    path('<int:pk>', DetalharCarrosView.as_view(), name='detalhar-carro'),
    path('atualizar/<int:pk>', AtualizarCarrosView.as_view(), name='atualizar-carro'),
    path('deletar/<int:pk>', DeletarCarrosView.as_view(), name='deletar-carro'),
    path('novo_aluguel/', CriarAluguelView.as_view(), name='cadastrar-aluguel'), 
   ] 