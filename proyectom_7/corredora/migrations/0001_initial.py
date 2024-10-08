# Generated by Django 5.0.7 on 2024-08-18 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoInmueble',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'estado_inmueble',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('m2_construidos', models.IntegerField()),
                ('m2_totales', models.IntegerField()),
                ('cantidad_estacionamientos', models.IntegerField()),
                ('cantidad_habitaciones', models.IntegerField()),
                ('cantidad_banos', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('valor_mensual_arriendo', models.IntegerField()),
            ],
            options={
                'db_table': 'inmueble',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoInmueble',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tipo_inmueble',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tipo_usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
                ('activo', models.BooleanField(blank=True, null=True)),
                ('creacion_registro', models.DateTimeField(blank=True, null=True)),
                ('modificacion_registro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioInmueble',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'usuario_inmueble',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioPublicaArriendoInmueble',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('creacion_registro', models.DateTimeField(blank=True, null=True)),
                ('modificacion_registro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuario_publica_arriendo_inmueble',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioSolicitaArrendarInmueble',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('creacion_registro', models.DateTimeField(blank=True, null=True)),
                ('modificacion_registro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuario_solicita_arrendar_inmueble',
                'managed': False,
            },
        ),
    ]
