from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto, Empresa
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Vistas para Producto

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'inventario/producto_list.html'
    context_object_name = 'productos'

class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = 'inventario/producto_detail.html'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'sku', 'stock', 'empresa']
    template_name = 'inventario/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'sku', 'stock', 'empresa']
    template_name = 'inventario/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'inventario/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')

# Vistas para Empresa

class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'inventario/empresa_list.html'
    context_object_name = 'empresas'

class EmpresaDetailView(LoginRequiredMixin, DetailView):
    model = Empresa
    template_name = 'inventario/empresa_detail.html'

class EmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresa
    fields = ['nombre', 'contacto', 'email', 'telefono']
    template_name = 'inventario/empresa_form.html'
    success_url = reverse_lazy('empresa_list')

class EmpresaUpdateView(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = ['nombre', 'contacto', 'email', 'telefono']
    template_name = 'inventario/empresa_form.html'
    success_url = reverse_lazy('empresa_list')

class EmpresaDeleteView(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = 'inventario/empresa_confirm_delete.html'
    success_url = reverse_lazy('empresa_list')
