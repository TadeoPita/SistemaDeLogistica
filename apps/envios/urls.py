from django.urls import path
from .views import (
    EnvioListView,
    EnvioDetailView,
    EnvioCreateView,
    EnvioUpdateView,
    EnvioDeleteView,
    envio_events_json
)

urlpatterns = [
    path('', EnvioListView.as_view(), name='envio_list'),
    path('events/', envio_events_json, name='envio_events'),
    path('<int:pk>/', EnvioDetailView.as_view(), name='envio_detail'),
    path('crear/', EnvioCreateView.as_view(), name='envio_create'),
    path('<int:pk>/editar/', EnvioUpdateView.as_view(), name='envio_update'),
    path('<int:pk>/eliminar/', EnvioDeleteView.as_view(), name='envio_delete'),
]
