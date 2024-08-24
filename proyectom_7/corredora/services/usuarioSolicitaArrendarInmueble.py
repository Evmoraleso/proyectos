# import datetime
# from django.db import transaction
# from corredora.models import Inmueble, UsuarioSolicitaArrendarInmueble
# from corredora.services.inmueble import actualizar_estado_inmueble
# import logging


# logging.basicConfig(level=logging.DEBUG)

# def add_solicitud(id_usuario, id_inmueble):
#     try:
#         with transaction.atomic():
#             logging.debug("pasa por el servicio crear arriendo")
#             logging.debug(id_usuario)
#             logging.debug(id_inmueble)
#             solicitud = UsuarioSolicitaArrendarInmueble.objects.create(usuario_id=id_usuario, inmueble_id=id_inmueble, creacion_registro=datetime.datetime.now(), modificacion_registro=datetime.datetime.now())
#             solicitud.save()
#             actualiza_estado = actualizar_estado_inmueble(id_inmueble)                
#     except Exception as e:
#         raise