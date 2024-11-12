from django.urls import path
from .views import (
    ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    DireccionListView, DireccionDetailView, DireccionCreateView, DireccionUpdateView, DireccionDeleteView,
)

urlpatterns = [
    # URLs para Cliente
    path('', ClienteListView.as_view(), name='cliente_list'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # URLs para Dirección
    path('direcciones/', DireccionListView.as_view(), name='direccion_list'),
    path('direcciones/<int:pk>/', DireccionDetailView.as_view(), name='direccion_detail'),
    path('direcciones/nueva/', DireccionCreateView.as_view(), name='direccion_create'),
    path('direcciones/<int:pk>/editar/', DireccionUpdateView.as_view(), name='direccion_update'),
    path('direcciones/<int:pk>/eliminar/', DireccionDeleteView.as_view(), name='direccion_delete'),
]
