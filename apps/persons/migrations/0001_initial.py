# Generated by Django 4.0.4 on 2022-07-21 01:55

import apps.main.modules.images
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='DNI')),
                ('nombres', models.CharField(max_length=250, verbose_name='Nombres')),
                ('apellido_paterno', models.CharField(max_length=250, verbose_name='Apellido paterno')),
                ('apellido_materno', models.CharField(max_length=250, verbose_name='Apellido materno')),
                ('fecha_nacimiento', models.DateField(default=None, verbose_name='Fecha de nacimiento')),
                ('genero', models.CharField(choices=[('FEM', 'FEMENINO'), ('MAS', 'MASCULINO')], default='MAS', max_length=10, verbose_name='Género')),
                ('estado_civil', models.CharField(choices=[('CAS', 'CASADO'), ('DIV', 'DIVORCIADO'), ('SOL', 'SOLTERO')], default='SOL', max_length=200, verbose_name='Estado civil')),
                ('foto', models.ImageField(blank=True, null=True, upload_to=apps.main.modules.images.renombrar_imagen, verbose_name='Foto')),
                ('correo_institucional', models.EmailField(blank=True, max_length=150, null=True, verbose_name='Correo electrónico institucional')),
                ('correo_personal', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo electrónico personal')),
                ('telefono_principal', models.CharField(blank=True, max_length=9, null=True, verbose_name='Nro de Teléfono institucional')),
                ('telefono_secundario', models.CharField(blank=True, max_length=9, null=True, verbose_name='Nro de Teléfono personal')),
                ('anexo_institucional', models.CharField(blank=True, max_length=10, null=True, verbose_name='Anexo telefónico')),
                ('direccion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Direccion')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
