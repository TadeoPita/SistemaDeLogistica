from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from .models import Orden, DetalleOrden
from .forms import OrdenForm, DetalleOrdenFormSet


class OrdenListView(LoginRequiredMixin, ListView):
    model = Orden
    template_name = 'ordenes/orden_list.html'
    context_object_name = 'ordenes'

class OrdenDetailView(LoginRequiredMixin, DetailView):
    model = Orden
    template_name = 'ordenes/orden_detail.html'
    context_object_name = 'orden'

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
            data['detalles'] = DetalleOrdenFormSet(queryset=DetalleOrden.objects.none())
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
            else:
                return self.form_invalid(form)
        return super().form_valid(form)


class OrdenUpdateView(LoginRequiredMixin, UpdateView):
    model = Orden
    form_class = OrdenForm
    template_name = 'ordenes/orden_form.html'
    success_url = reverse_lazy('orden_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['detalles'] = DetalleOrdenFormSet(self.request.POST, instance=self.object)
        else:
            data['detalles'] = DetalleOrdenFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        detalles = context['detalles']
        with transaction.atomic():
            self.object = form.save()
            if detalles.is_valid():
                detalles.instance = self.object
                detalles.save()
            else:
                return self.form_invalid(form)
        return super().form_valid(form)



class OrdenDeleteView(LoginRequiredMixin, DeleteView):
    model = Orden
    template_name = 'ordenes/orden_confirm_delete.html'
    success_url = reverse_lazy('orden_list')
