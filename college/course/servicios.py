from django.utils import timezone
from .models import Profesor, Estudiante, Direccion, Curso, EstudianteCurso, ProfesorCurso

def crear_curso(codigo, nombre, version):
    curso = Curso.objects.create(codigo=codigo,nombre=nombre,version=version)
    return curso

def crear_profesor(rut, nombre, apellido, creado_por):
    profesor = Profesor.objects.create(rut=rut,nombre=nombre,apellido=apellido,activo=True,creacion_registro=timezone.now(),modificacion_registro=None,creado_por=creado_por)
    return profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac, creado_por):
    estudiante = Estudiante.objects.create(rut=rut,nombre=nombre,apellido=apellido, fecha_nac=fecha_nac ,activo=True,creacion_registro=timezone.now(),modificacion_registro=None,creado_por=creado_por)
    return estudiante

def crear_direccion(id, calle, numero, dpto, comuna, ciudad, region, estudiante):
    direccion = Direccion.objects.create(id=id, calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)
    return direccion

def asignar_profesor_curso(profesor, curso):
    profesor_curso= ProfesorCurso.objects.create(profesor=profesor, curso=curso)
    return profesor_curso

def asignar_estudiante_curso(estudiante, curso):
    estudiante_curso= EstudianteCurso.objects.create(estudiante=estudiante, curso=curso)
    return estudiante_curso

def obtener_curso(codigo) -> Curso:
    curso=Curso.objects.get(codigo=codigo)
    return curso

def obtener_profesor(rut) -> Profesor:
    profesor=Profesor.objects.get(rut=rut)
    return profesor

def obtener_estudiante(rut) -> Estudiante:
    estudiante=Estudiante.objects.get(rut=rut)
    return estudiante

def imprimir_estudiante_curso():
    resultados = EstudianteCurso.objects.select_related('estudiante', 'curso').values(
        'estudiante__rut',
        'estudiante__nombre',
        'estudiante__apellido',
        'estudiante__activo',
        'curso__codigo',
        'curso__nombre',
        'curso__version'
    )
    for resultado in resultados:
            print(f"Estudiante: {resultado['estudiante__nombre']} {resultado['estudiante__apellido']}")
            print(f"  - Rut: {resultado['estudiante__rut']}")
            print(f"  - Activo: {'Sí' if resultado['estudiante__activo'] else 'No'}")
            print(f"Curso: {resultado['curso__nombre']}")
            print(f"  - Codigo: {resultado['curso__codigo']}")
            print(f"  - Versión: {resultado['curso__version']}")
            print("-" * 30)