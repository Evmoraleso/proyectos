from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from corredora.services.usuario import add, obtener_usuario
from django.contrib.auth import authenticate, login as auth_login, logout
import logging

logging.basicConfig(level=logging.DEBUG)

# Create your views here.
def signup(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        idTipoUsuario = request.POST.get('tipo_usuario')
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.warning(request, 'Las contraseñas no coinciden.')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'El email ya existe.')
        elif User.objects.filter(username=username).exists():
            messages.warning(request, 'El nombre de usuario ya existe.')
        else:
            add(rut, nombres, apellidos, direccion, telefono, email, username, password, idTipoUsuario)
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('login')
                
                
        return render(request, 'registrationapp/registration.html', {
            'rut': rut,
            'nombres': nombres,
            'apellidos': apellidos,
            'direccion': direccion,
            'telefono': telefono,
            'email': email,
            'tipo_usuario': idTipoUsuario,
            'username': username,
        })
    else:
        return render(request, 'registrationapp/registration.html')

def login(request):
    logging.debug("Entrando en loging")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            usuario_= obtener_usuario(user)
            if usuario_.tipo_usuario.id == 1:
                logging.debug("renderiza a la vista arrendatario")
                return redirect('/arrendatario/perfil_usuario_arrendatario', user=user, usuario=usuario_)               
            else:
                return redirect('/arrendador/perfil_usuario_arrendador', user=user, usuario=usuario_) 
        else:
            logging.debug("pasa por el else de no usuario")
            messages.warning(request, 'Username or password do not match')
            return redirect('login')
    else:
        logging.debug("rpara por el else de si no es post")
        return render(request, 'registrationapp/login.html')

def logged_out(request):
    logout(request)
    return render(request, 'registrationapp/logged_out.html')

