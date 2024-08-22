from django.urls import include, path
from . import views

urlpatterns = [

    path('registratioapp/', include('django.contrib.auth.urls')),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logged_out, name='logout'),  
