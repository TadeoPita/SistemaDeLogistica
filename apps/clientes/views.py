from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Direccion
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import ClienteForm

class HomeView(TemplateView):
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
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direccion_fields'] = ['calle', 'numero', 'departamento', 'ciudad', 'provincia', 'codigo_postal']
        return context

    def form_valid(self, form):
        # Primero, creamos la dirección
        direccion = Direccion.objects.create(
            calle=form.cleaned_data['calle'],
            numero=form.cleaned_data['numero'],
            departamento=form.cleaned_data.get('departamento', ''),
            ciudad=form.cleaned_data['ciudad'],
            provincia=form.cleaned_data['provincia'],
            codigo_postal=form.cleaned_data['codigo_postal']
        )
        # Luego, asignamos la dirección al cliente y lo guardamos
        cliente = form.save(commit=False)
        cliente.direccion = direccion
        cliente.save()
        return super().form_valid(form)

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direccion_fields'] = ['calle', 'numero', 'departamento', 'ciudad', 'provincia', 'codigo_postal']
        return context

    def get_initial(self):
        initial = super().get_initial()
        if self.object.direccion:
            direccion = self.object.direccion
            initial['calle'] = direccion.calle
            initial['numero'] = direccion.numero
            initial['departamento'] = direccion.departamento
            initial['ciudad'] = direccion.ciudad
            initial['provincia'] = direccion.provincia
            initial['codigo_postal'] = direccion.codigo_postal
        return initial

    def form_valid(self, form):
        # Actualizamos la dirección existente o creamos una nueva si no existe
        if self.object.direccion:
            direccion = self.object.direccion
            direccion.calle = form.cleaned_data['calle']
            direccion.numero = form.cleaned_data['numero']
            direccion.departamento = form.cleaned_data.get('departamento', '')
            direccion.ciudad = form.cleaned_data['ciudad']
            direccion.provincia = form.cleaned_data['provincia']
            direccion.codigo_postal = form.cleaned_data['codigo_postal']
            direccion.save()
        else:
            direccion = Direccion.objects.create(
                calle=form.cleaned_data['calle'],
                numero=form.cleaned_data['numero'],
                departamento=form.cleaned_data.get('departamento', ''),
                ciudad=form.cleaned_data['ciudad'],
                provincia=form.cleaned_data['provincia'],
                codigo_postal=form.cleaned_data['codigo_postal']
            )
            self.object.direccion = direccion
            self.object.save()
        return super().form_valid(form)

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

# Vistas para Dirección (si las necesitas)

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
