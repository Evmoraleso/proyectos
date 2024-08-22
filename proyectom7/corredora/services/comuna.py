from urllib import request
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User
from corredora.models import Comuna

def obtener_comunas():
    try:
        comunas = Comuna.objects.all()
        return comunas
    except Comuna.DoesNotExist:
        return None

def obtener_comuna(comuna_id):
    try:
        comuna = Comuna.objects.get(id=comuna_id)
        return comuna
    except Comuna.DoesNotExist:
        return None