from django.db import transaction
from corredora.models import Inmueble, UsuarioInmueble
import logging

from corredora.services.usuario import obtener_usuario

logging.basicConfig(level=logging.DEBUG)

def add(id_usuario, nombre, descripcion, m2_construidos, m2_totales, cantidad_estacionamientos, cantidad_habitaciones, cantidad_banos, direccion, comuna_id, valor_mensual_arriendo, estado_inmueble_id, tipo_inmueble_id):
    try:
        with transaction.atomic():
            inmbueble = Inmueble.objects.create(nombre=nombre, descripcion=descripcion, m2_construidos=m2_construidos, m2_totales=m2_totales, cantidad_estacionamientos=cantidad_estacionamientos, cantidad_habitaciones=cantidad_habitaciones, cantidad_banos=cantidad_banos, direccion=direccion, comuna_id=comuna_id, valor_mensual_arriendo=valor_mensual_arriendo, estado_inmueble_id=estado_inmueble_id, tipo_inmueble_id=tipo_inmueble_id)
            inmbueble.save()
            id_inmueble=Inmueble.objects.latest('id')       
            usuario_inmueble=UsuarioInmueble.objects.create(usuario_id=id_usuario,inmueble_id=id_inmueble.id) 
            usuario_inmueble.save()  
    except Exception as e:
        raise

def update(inmueble_id, nombre, descripcion, m2_construidos, m2_totales, cantidad_estacionamientos, cantidad_habitaciones, cantidad_banos, direccion, comuna_id, valor_mensual_arriendo, estado_inmueble_id, tipo_inmueble_id):
    logging.debug("pasa por el servicio update inmueble")
    try:
        Inmueble.objects.filter(id=inmueble_id).update(
            nombre=nombre,
            descripcion=descripcion,
            m2_construidos=m2_construidos,
            m2_totales=m2_totales,
            cantidad_estacionamientos=cantidad_estacionamientos,
            cantidad_habitaciones=cantidad_habitaciones,
            cantidad_banos=cantidad_banos,
            direccion=direccion,
            comuna_id=comuna_id,
            valor_mensual_arriendo=valor_mensual_arriendo,
            estado_inmueble_id=estado_inmueble_id,
            tipo_inmueble_id=tipo_inmueble_id
            )
    except Exception as e:
        raise
        
def obtener_inmueble_id(inmueble_id):
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        return inmueble
    except Inmueble.DoesNotExist:
        return None
    
def obtener_inmueble():
    try:
        inmueble=Inmueble.objects.latest('id') 
        return inmueble
    except Inmueble.DoesNotExist:
        return None

def obtener_inmuebles_usuario(usuario):
    usuario_sys = obtener_usuario(usuario)
    logging.debug("idusuairo")
    logging.debug(usuario_sys.rut) 
    inmuebles = Inmueble.objects.filter(usuarioinmueble__usuario=usuario_sys.rut)
    return inmuebles

def obtener_inmuebles():
    inmuebles = Inmueble.objects.filter(estado_inmueble_id=1)
    return inmuebles

def delete(inmueble_id):
    logging.debug("Intentando eliminar inmueble con ID: %s", inmueble_id)
    try:
        if delete_usuario_inmueble(inmueble_id):
            inmueble = Inmueble.objects.get(id=inmueble_id)
            inmueble.delete()
            logging.debug("Inmueble eliminado exitosamente")
            return True
    except Inmueble.DoesNotExist:
        logging.error("Inmueble con ID %s no existe", inmueble_id)
        raise
    except Exception as e:
        raise

def delete_usuario_inmueble(inmueble_id):
    logging.debug("Intentando eliminar usuario inmueble con ID: %s", inmueble_id)
    try:
        usuario_inmueble = UsuarioInmueble.objects.get(inmueble_id=inmueble_id)
        logging.debug(usuario_inmueble)
        usuario_inmueble.delete()
        logging.debug("usuario Inmueble eliminado exitosamente")
        return True
    except Inmueble.DoesNotExist:
        logging.error("Usuario Inmueble con ID %s no existe", inmueble_id)
        raise
    except Exception as e:
        raise

def actualizar_estado_inmueble(inmueble_id):
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        inmueble.estado_inmueble_id = 5
        inmueble.save()
        return True
    except Inmueble.DoesNotExist:
        return False