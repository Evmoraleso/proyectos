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

def obtener_comunas_regiones(region_id):
    try:
        comunas_regiones= Comuna.objects.filter(id=region_id)
        return comunas_regiones
    except Comuna.DoesNotExist:
        return None