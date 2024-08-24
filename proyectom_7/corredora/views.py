from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from corredora.services.usuario import update, obtener_usuario
from corredora.services.comuna import obtener_comunas
from corredora.services.estadoInmueble import obtener_estado_inmuebles
from corredora.services.tipoInmueble import obtener_tipo_inmuebles
from corredora.services.inmueble import add, update, delete, obtener_inmuebles_usuario, obtener_inmueble_id,obtener_inmuebles
from corredora.services.region import obtener_regiones
# from corredora.services.usuarioSolicitaArrendarInmueble import add_solicitud
import pdb
import logging
# Create your views here.
logging.basicConfig(level=logging.DEBUG)

@login_required
def perfil_usuario_arrendatario(request):
    usuario = obtener_usuario(request.user)
    return render(request, 'arrendatario/perfil_usuario_arrendatario.html', {'usuario': usuario})

@login_required
def perfil_usuario_arrendador(request):
    usuario = obtener_usuario(request.user)
    return render(request, 'arrendador/perfil_usuario_arrendador.html', {'usuario': usuario})

@login_required
def actualizar_perfil(request):
    usuario = obtener_usuario(request.user)
    if request.method == 'POST':
        rut = request.POST['rut']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        tipo_usuario = request.POST.get('tipo_usuario')

        update(rut, nombres, apellidos, direccion, telefono, tipo_usuario)
        messages.success(request, 'Datos actualizados exitosamente.')
        return redirect('/actualizar_perfil')
    
    return render(request, 'actualizar_perfil.html', {'usuario': usuario})

@login_required
def agregar_inmueble(request):
    usuario = obtener_usuario(request.user)
    if request.method == 'POST':
        logging.debug("usuairo")
        logging.debug(request.user)
        logging.debug("NOMBRE")
        logging.debug(request.POST['nombre'])
        # try:
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        m2_construidos = request.POST['m2_construidos']
        m2_totales = request.POST['m2_totales']
        cantidad_estacionamientos = request.POST['cantidad_estacionamientos']
        cantidad_habitaciones = request.POST['cantidad_habitaciones']
        cantidad_banos = request.POST['cantidad_banos']
        direccion = request.POST['direccion']
        comuna_id = request.POST['comuna']
        valor_mensual_arriendo = request.POST['valor_mensual_arriendo']
        estado_inmueble_id = request.POST['estado_inmueble']
        tipo_inmueble_id = request.POST['tipo_inmueble']
        rut=obtener_usuario(request.user)
        logging.debug("rut")
        logging.debug(rut)
            
        add(
            id_usuario=rut.rut,
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

        messages.success(request, 'Inmueble creado exitosamente.')
        return redirect('/arrendador/agregar_inmueble')
        
        # except Exception as e:
        messages.error(request, f"Error al crear el inmueble: {str(e)}")
            
    comunas = obtener_comunas()
    estados_inmueble = obtener_estado_inmuebles()
    tipos_inmueble = obtener_tipo_inmuebles()
    return render(request, 'arrendador/agregar_inmueble.html', {
            'comunas': comunas,
            'estados_inmueble': estados_inmueble,
            'tipos_inmueble': tipos_inmueble, 
            'usuario': usuario
        })
        
@login_required
def listar_inmuebles_usuario(request):
    usuario = obtener_usuario(request.user)
    inmuebles = obtener_inmuebles_usuario(request.user)
    return render(request, 'arrendador/listar_inmuebles_usuario.html', {'inmuebles': inmuebles, 'usuario': usuario})

@login_required
def actualizar_inmueble(request, inmueble_id):
    usuario = obtener_usuario(request.user)
    logging.debug("actualizar_inmueble")
    logging.debug(inmueble_id)

    inmueble = obtener_inmueble_id(inmueble_id)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        m2_construidos = request.POST['m2_construidos']
        m2_totales = request.POST['m2_totales']
        cantidad_estacionamientos = request.POST['cantidad_estacionamientos']
        cantidad_habitaciones = request.POST['cantidad_habitaciones']
        cantidad_banos = request.POST['cantidad_banos']
        direccion = request.POST['direccion']
        comuna_id = request.POST.get('comuna')
        valor_mensual_arriendo = request.POST['valor_mensual_arriendo']
        estado_inmueble_id = request.POST.get('estado_inmueble')
        tipo_inmueble_id = request.POST.get('tipo_inmueble')
        update(inmueble_id, nombre, descripcion, m2_construidos, m2_totales, cantidad_estacionamientos, cantidad_habitaciones, cantidad_banos, direccion, comuna_id, valor_mensual_arriendo, estado_inmueble_id, tipo_inmueble_id)
        
        messages.success(request, 'Inmueble actualizado exitosamente.')
        return redirect('/arrendador/listar_inmuebles_usuario')

    comunas = obtener_comunas()
    estados_inmueble = obtener_estado_inmuebles()
    tipos_inmueble = obtener_tipo_inmuebles()
    return render(request, 'arrendador/actualizar_inmueble.html', {
        'usuario': usuario,
        'inmueble': inmueble,
        'comunas': comunas,
        'estados_inmueble': estados_inmueble,
        'tipos_inmueble': tipos_inmueble
    })

@login_required
def eliminar_inmueble(request, inmueble_id):
    logging.debug("eliminar inmueble")
    logging.debug(inmueble_id)
    if request.method == 'POST':
        logging.debug("pasa el POST")
        delete(inmueble_id)
    
        messages.success(request, 'Inmueble eliminado exitosamente.')
        return redirect('/arrendador/listar_inmuebles_usuario')
    logging.debug("SALTA el POST")    
    inmuebles = obtener_inmuebles_usuario(request.user)
    return render(request, 'arrendador/listar_inmuebles_usuario.html', {'inmuebles': inmuebles})

@login_required
def listar_inmuebles_disponibles(request):
    usuario = obtener_usuario(request.user)
    regiones = obtener_regiones()
    comunas = obtener_comunas()
    inmuebles = obtener_inmuebles()

    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')

    if region_id:
        comunas = comunas.filter(region_id=region_id)
        inmuebles = inmuebles.filter(comuna__region_id=region_id)
    
    if comuna_id:
        inmuebles = inmuebles.filter(comuna_id=comuna_id)

    context = {
        'usuario': usuario,
        'regiones': regiones,
        'comunas': comunas,
        'inmuebles': inmuebles,
        'selected_region': region_id,
        'selected_comuna': comuna_id,
    }
    return render(request, 'arrendatario/listar_inmuebles_disponibles.html', context)    
