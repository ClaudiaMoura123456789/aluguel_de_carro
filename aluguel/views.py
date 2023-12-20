from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Carro, Aluguel
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CarroForm, RegistrationForm, AluguelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class HomeTemplateView(TemplateView):
    template_name='home.html'

class ListaCarrosView(ListView):
    template_name = 'carro/listar.html'
    model=Carro
    context_object_name='carros'
    paginate_by = 5

class DetalharCarrosView(DetailView):
    template_name = 'carro/detalhar.html'
    model=Carro
    context_object_name='carro'

class CriarCarrosView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'carro/cadastrar.html'
    model=Carro
    form_class=CarroForm
    permission_required = 'aluguel.add_carro'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro cadastrado com sucesso")
        return reverse('listar-carro')
    
class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    model = get_user_model()
    form_class = RegistrationForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso!")
        return reverse('home')
class AtualizarCarrosView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'carro/atualizar.html'
    model=Carro
    form_class=CarroForm
    permission_required = 'aluguel.carro.change'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro atualizar com sucesso")
        return reverse('listar-carro')
    
class DeletarCarrosView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'carro/carro_confirm_delete.html'
    model=Carro
    permission_required = 'aluguel.carro.delete'
  

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro deletado com sucesso")
        return reverse('listar-carro')    
    
class CriarAluguelView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'aluguel/cadastrar.html'
    model=Aluguel
    form_class=AluguelForm
    permission_required = 'aluguel.add_aluguel'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro alugado com sucesso")
        return reverse('listar-carro')    
    



# class CriarReservaView(View):
#     template_name = 'criar_reserva.html'

#     def get(self, request, carro_id):
#         carro = get_object_or_404(Car, pk=carro_id, disponivel=True)
#         return render(request, self.template_name, {'carro': carro})
#     def post(self, request, carro_id):
#         carro = get_object_or_404(Car, pk=carro_id, disponivel=True)
#         # Lógica para criar uma reserva (pode ser adicionada aqui)
#         # ...
#         return HttpResponseRedirect(reverse('lista_carros'))
