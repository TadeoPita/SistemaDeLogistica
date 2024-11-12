from django.contrib import admin
from django.urls import path, include
from apps.clientes.views import HomeView 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('clientes/', include('apps.clientes.urls')),
    path('inventario/', include('apps.inventario.urls')),
    path('ordenes/', include('apps.ordenes.urls')),
    path('envios/', include('apps.envios.urls')),
    path('seguimiento/', include('apps.seguimiento.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
