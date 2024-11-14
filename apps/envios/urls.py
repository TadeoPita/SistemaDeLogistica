from django.urls import path
from .views import (
    EnvioListView,
    EnvioDetailView,
    EnvioCreateView,
    EnvioUpdateView,
    EnvioDeleteView,
)

urlpatterns = [
    path('', EnvioListView.as_view(), name='envio_list'),
    path('<int:pk>/', EnvioDetailView.as_view(), name='envio_detail'),
    path('crear/', EnvioCreateView.as_view(), name='envio_create'),
    path('<int:pk>/editar/', EnvioUpdateView.as_view(), name='envio_update'),
    path('<int:pk>/eliminar/', EnvioDeleteView.as_view(), name='envio_delete'),
]
