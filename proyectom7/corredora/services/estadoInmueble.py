from urllib import request
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User
from corredora.models import EstadoInmueble

def obtener_estado_inmuebles():
    try:
        estado = EstadoInmueble.objects.all()
        return estado
    except EstadoInmueble.DoesNotExist:
        return None

def obtener_estado_inmueble(estado_inmueble_id):
    try:
        estado = EstadoInmueble.objects.get(id=estado_inmueble_id)
        return estado
    except EstadoInmueble.DoesNotExist:
        return None