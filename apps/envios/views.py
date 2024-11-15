from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Envio
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.timezone import localtime

class EnvioListView(LoginRequiredMixin, ListView):
    model = Envio
    template_name = 'envios/envio_list.html'
    context_object_name = 'envios'

def envio_events_json(request):
    envios = Envio.objects.all()
    eventos = []
    for envio in envios:
        color = ''
        if envio.estado == 'Preparando':
            color = 'red'
        elif envio.estado == 'En camino':
            color = 'orange'
        elif envio.estado == 'Entregado':
            color = 'green'

        eventos.append({
            'title': f'Orden #{envio.orden.id} - {envio.estado}',
            'start': localtime(envio.fecha_envio).isoformat(),  # Convierte a la hora local
            'end': localtime(envio.fecha_entrega).isoformat(),  # Convierte a la hora local
            'estado': envio.estado,
            'orden_id': envio.orden.id,
            'color': color,
        })
    return JsonResponse(eventos, safe=False)


class EnvioDetailView(LoginRequiredMixin, DetailView):
    model = Envio
    template_name = 'envios/envio_detail.html'

class EnvioCreateView(LoginRequiredMixin, CreateView):
    model = Envio
    fields = ['orden', 'estado', 'fecha_envio', 'fecha_entrega']
    template_name = 'envios/envio_form.html'
    success_url = reverse_lazy('envio_list')

class EnvioUpdateView(LoginRequiredMixin, UpdateView):
    model = Envio
    fields = ['estado', 'fecha_envio', 'fecha_entrega']
    template_name = 'envios/envio_form.html'
    success_url = reverse_lazy('envio_list')

class EnvioDeleteView(LoginRequiredMixin, DeleteView):
    model = Envio
    template_name = 'envios/envio_confirm_delete.html'
    success_url = reverse_lazy('envio_list')
