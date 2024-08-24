# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comuna(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey('Region', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comuna'


class EstadoInmueble(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado_inmueble'


class Inmueble(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    m2_construidos = models.IntegerField()
    m2_totales = models.IntegerField()
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING)
    valor_mensual_arriendo = models.IntegerField()
    estado_inmueble = models.ForeignKey(EstadoInmueble, models.DO_NOTHING)
    tipo_inmueble = models.ForeignKey('TipoInmueble', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inmueble'


class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'region'


class TipoInmueble(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_inmueble'


class TipoUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    activo = models.BooleanField(blank=True, null=True)
    creacion_registro = models.DateTimeField(blank=True, null=True)
    modificacion_registro = models.DateTimeField(blank=True, null=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioInmueble(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING)
    inmueble = models.ForeignKey(Inmueble, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario_inmueble'


class UsuarioPublicaArriendoInmueble(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING)
    inmueble = models.ForeignKey(Inmueble, models.DO_NOTHING)
    creacion_registro = models.DateTimeField(blank=True, null=True)
    modificacion_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_publica_arriendo_inmueble'


class UsuarioSolicitaArrendarInmueble(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING)
    inmueble = models.ForeignKey(Inmueble, models.DO_NOTHING)
    creacion_registro = models.DateTimeField(blank=True, null=True)
    modificacion_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_solicita_arrendar_inmueble'
