from corredora.models import Region

def obtener_regiones():
    try:
        regiones = Region.objects.all()
        return regiones
    except Region.DoesNotExist:
        return None

def obtener_region(region_id):
    try:
        regione = Region.objects.get(id=region_id)
        return regione
    except Region.DoesNotExist:
        return None