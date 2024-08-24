from django.urls import include, path
from . import views

urlpatterns = [

    path('registratioapp/', include('django.contrib.auth.urls')),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    # path('index/', views.index, name='index'),
    path('logout/', views.logged_out, name='logout'),  
    # path('perfil_usuario_arrendatario/', views.perfil_usuario_arrendatario, name='perfil_usuario_arrendatario'),
    # path('perfil_usuario_arrendador/', views.perfil_usuario_arrendador, name='perfil_usuario_arrendador'),
]
