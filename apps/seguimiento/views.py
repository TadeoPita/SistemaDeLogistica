from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from .forms import SeguimientoForm
from ordenes.models import Orden
from django.shortcuts import get_object_or_404, redirect

class SeguimientoFormView(FormView):
    template_name = 'seguimiento/seguimiento_form.html'
    form_class = SeguimientoForm

    def form_valid(self, form):
        codigo = form.cleaned_data['codigo_seguimiento']
        return redirect('seguimiento_detail', codigo_seguimiento=codigo)

class SeguimientoDetailView(DetailView):
    model = Orden
    template_name = 'seguimiento/seguimiento_detail.html'
    context_object_name = 'orden'

    def get_object(self):
        codigo_seguimiento = self.kwargs['codigo_seguimiento']
        return get_object_or_404(Orden, codigo_seguimiento=codigo_seguimiento)
