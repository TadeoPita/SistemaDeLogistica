from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Orden, DetalleOrden
from .forms import OrdenForm, DetalleOrdenFormSet
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db import transaction

class OrdenListView(LoginRequiredMixin, ListView):
    model = Orden
    template_name = 'ordenes/orden_list.html'
    context_object_name = 'ordenes'

class OrdenDetailView(LoginRequiredMixin, DetailView):
    model = Orden
    template_name = 'ordenes/orden_detail.html'

class OrdenCreateView(LoginRequiredMixin, CreateView):
    model = Orden
    form_class = OrdenForm
    template_name = 'ordenes/orden_form.html'
    success_url = reverse_lazy('orden_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['detalles'] = DetalleOrdenFormSet(self.request.POST)
        else:
            data['detalles'] = DetalleOrdenFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        detalles = context['detalles']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if detalles.is_valid():
                detalles.instance = self.object
                detalles.save()
        return super().form_valid(form)
