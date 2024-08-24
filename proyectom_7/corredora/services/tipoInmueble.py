from corredora.models import TipoInmueble

def obtener_tipo_inmuebles():
    try:
        tipo_inmueble = TipoInmueble.objects.all()
        return tipo_inmueble
    except TipoInmueble.DoesNotExist:
        return None

def obtener_tipo_inmueble(tipo_inmueble_id):
    try:
        tipo_inmueble = TipoInmueble.objects.get(id=tipo_inmueble_id)
        return tipo_inmueble
    except TipoInmueble.DoesNotExist:
        return None