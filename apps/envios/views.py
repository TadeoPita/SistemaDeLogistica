from django.views.generic import ListView, DetailView, UpdateView
from .models import Envio
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class EnvioListView(LoginRequiredMixin, ListView):
    model = Envio
    template_name = 'envios/envio_list.html'
    context_object_name = 'envios'

class EnvioDetailView(LoginRequiredMixin, DetailView):
    model = Envio
    template_name = 'envios/envio_detail.html'

class EnvioUpdateView(LoginRequiredMixin, UpdateView):
    model = Envio
    fields = ['estado', 'fecha_envio', 'fecha_entrega']
    template_name = 'envios/envio_form.html'
    success_url = reverse_lazy('envio_list')
