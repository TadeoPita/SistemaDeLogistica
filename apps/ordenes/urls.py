from django.urls import path
from .views import OrdenListView, OrdenDetailView, OrdenCreateView, OrdenUpdateView, OrdenDeleteView
urlpatterns = [
    path('', OrdenListView.as_view(), name='orden_list'),
    path('<int:pk>/', OrdenDetailView.as_view(), name='orden_detail'),
    path('crear/', OrdenCreateView.as_view(), name='orden_create'),
    path('<int:pk>/editar/', OrdenUpdateView.as_view(), name='orden_edit'),
    path('<int:pk>/eliminar/', OrdenDeleteView.as_view(), name='orden_delete'),
]
