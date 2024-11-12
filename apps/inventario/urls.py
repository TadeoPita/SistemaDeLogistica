from django.urls import path
from .views import (
    ProductoListView, ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView,
    EmpresaListView, EmpresaDetailView, EmpresaCreateView, EmpresaUpdateView, EmpresaDeleteView,
)

urlpatterns = [
    # URLs para Producto
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),

    # URLs para Empresa
    path('empresas/', EmpresaListView.as_view(), name='empresa_list'),
    path('empresas/<int:pk>/', EmpresaDetailView.as_view(), name='empresa_detail'),
    path('empresas/nueva/', EmpresaCreateView.as_view(), name='empresa_create'),
    path('empresas/<int:pk>/editar/', EmpresaUpdateView.as_view(), name='empresa_update'),
    path('empresas/<int:pk>/eliminar/', EmpresaDeleteView.as_view(), name='empresa_delete'),
]
