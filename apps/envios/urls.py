from django.urls import path
from .views import EnvioListView, EnvioDetailView, EnvioUpdateView

urlpatterns = [
    path('', EnvioListView.as_view(), name='envio_list'),
    path('<int:pk>/', EnvioDetailView.as_view(), name='envio_detail'),
    path('<int:pk>/editar/', EnvioUpdateView.as_view(), name='envio_update'),
]
