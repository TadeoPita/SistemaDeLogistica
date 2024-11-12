from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Direccion
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = '/login/' 


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes' 

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email', 'telefono', 'dni', 'direccion']
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email', 'telefono', 'dni', 'direccion']
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

# Vistas para Dirección

class DireccionListView(LoginRequiredMixin, ListView):
    model = Direccion
    template_name = 'clientes/direccion_list.html'
    context_object_name = 'direcciones'

class DireccionDetailView(LoginRequiredMixin, DetailView):
    model = Direccion
    template_name = 'clientes/direccion_detail.html'

class DireccionCreateView(LoginRequiredMixin, CreateView):
    model = Direccion
    fields = ['calle', 'numero', 'departamento', 'ciudad', 'provincia', 'codigo_postal']
    template_name = 'clientes/direccion_form.html'
    success_url = reverse_lazy('direccion_list')

class DireccionUpdateView(LoginRequiredMixin, UpdateView):
    model = Direccion
    fields = ['calle', 'numero', 'departamento', 'ciudad', 'provincia', 'codigo_postal']
    template_name = 'clientes/direccion_form.html'
    success_url = reverse_lazy('direccion_list')

class DireccionDeleteView(LoginRequiredMixin, DeleteView):
    model = Direccion
    template_name = 'clientes/direccion_confirm_delete.html'
    success_url = reverse_lazy('direccion_list')
