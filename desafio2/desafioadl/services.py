# servicios.py
import requests
from django.conf import settings

BASE_URL = settings.BASE_URL

def obtener_tareas():
    response = requests.get(f'{BASE_URL}/tareas/')
    return response.json()

def obtener_subtareas():
    response = requests.get(f'{BASE_URL}/subtareas/')
    return response.json()

def actualizar_tarea(pk, data):
    response = requests.patch(f'{BASE_URL}/tareas/{pk}/', json=data)
    return response.json()

def actualizar_subtarea(pk, data):
    response = requests.patch(f'{BASE_URL}/subtareas/{pk}/', json=data)
    return response.json()
