"""
URL configuration for proyectom7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from corredora import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registrationapp.urls')),
    path('actualizar_perfil/', views.actualizar_perfil, name='actualizar_perfil'),
    path('arrendador/agregar_inmueble/', views.agregar_inmueble, name='agregar_inmueble'),
    path('arrendador/listar_inmuebles_usuario/', views.listar_inmuebles_usuario, name='listar_inmuebles_usuario'),
    path('arrendatario/listar_inmuebles_disponibles/', views.listar_inmuebles_disponibles, name='listar_inmuebles_disponibles'),
    path('arrendador/actualizar_inmueble/<int:inmueble_id>/', views.actualizar_inmueble, name='actualizar_inmueble'),
    path('arrendador/eliminar_inmueble/<int:inmueble_id>/', views.eliminar_inmueble, name='eliminar_inmueble'),
    path('arrendatario/perfil_usuario_arrendatario/', views.perfil_usuario_arrendatario, name='perfil_usuario_arrendatario'),
    # path('arrendatario/solicitar_inmueble/<int:inmueble_id>/', views.solicitar_inmueble, name='solicitar_inmueble'),
    path('arrendador/perfil_usuario_arrendador/', views.perfil_usuario_arrendador, name='perfil_usuario_arrendador'),
]

