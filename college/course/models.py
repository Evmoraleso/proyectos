# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Profesor(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(blank=True, null=True)
    creacion_registro = models.DateTimeField(blank=True, null=True)
    modificacion_registro = models.DateTimeField(blank=True, null=True)
    creado_por = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'profesor'


class Estudiante(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(blank=True, null=True)
    creacion_registro = models.DateTimeField(blank=True, null=True)
    modificacion_registro = models.DateTimeField(blank=True, null=True)
    creado_por = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'


class Direccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'direccion'


class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class EstudianteCurso(models.Model):
    estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING)
    curso = models.ForeignKey(Curso, models.DO_NOTHING)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'estudiante_curso'


class ProfesorCurso(models.Model):
    profesor = models.ForeignKey(Profesor, models.DO_NOTHING)
    curso = models.ForeignKey(Curso, models.DO_NOTHING)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'profesor_curso'
