import datetime
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User
from corredora.models import Usuario, TipoUsuario
import logging

logging.basicConfig(level=logging.DEBUG)

def add(rut, nombres, apellidos, direccion, telefono, email, username, password, idTipoUsuario):
    try:
        with transaction.atomic():
            user = User.objects.create(first_name=nombres, last_name=apellidos, username=username, email=email)
            user.set_password(password) 
            user.save()
            tipoUsuario = TipoUsuario.objects.get(id=idTipoUsuario)    
            usuario = Usuario.objects.create(rut=rut,nombres=nombres, apellidos=apellidos, direccion=direccion, telefono=telefono, email=email, activo=True, creacion_registro=datetime.datetime.now(), modificacion_registro=datetime.datetime.now(), tipo_usuario=tipoUsuario)
            usuario.save()  
    except Exception as e:
            messages.error(f"Error al crear el usuario: {str(e)}")
            

def update(rut, nombres, apellidos, direccion, telefono, idTipoUsuario):
    logging.debug("pasa por el servicio update")
    try:
        with transaction.atomic():
            usuario = Usuario.objects.get(rut=rut)
            usuario.nombres = nombres
            usuario.apellidos = apellidos
            usuario.direccion = direccion
            usuario.telefono = telefono
            usuario.tipo_usuario = TipoUsuario.objects.get(id=idTipoUsuario)
            usuario.save()
    except Exception as e:
        messages.error(f"Error al actualizar usuario: {str(e)}")
        
def obtener_usuario(user):
    try:
        usuario = Usuario.objects.get(email=user.email)
        return usuario
    except Usuario.DoesNotExist:
        return None