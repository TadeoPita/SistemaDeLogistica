from django.urls import path
from .views import SeguimientoFormView, SeguimientoDetailView

urlpatterns = [
    path('', SeguimientoFormView.as_view(), name='seguimiento_form'),
    path('orden/<uuid:codigo_seguimiento>/', SeguimientoDetailView.as_view(), name='seguimiento_detail'),
]
