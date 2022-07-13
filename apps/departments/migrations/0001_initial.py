# Generated by Django 4.0.5 on 2022-07-13 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistritoJudicial',
            fields=[
                ('codigo', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Código')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('ubigeo', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Ubigeo')),
                ('latitud', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Latitud')),
                ('longitud', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Longitud')),
                ('ncpp', models.DateField(blank=True, default=None, null=True, verbose_name='NCPP')),
                ('nlpt', models.DateField(blank=True, default=None, null=True, verbose_name='NLPT')),
                ('corte', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Corte')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
            ],
            options={
                'verbose_name': 'Distrito Judicial',
                'verbose_name_plural': 'Distritos Judiciales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='ModuloCoordinacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Módulo o Coordinación')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
            ],
            options={
                'verbose_name': 'Módulo',
                'verbose_name_plural': 'Módulos',
            },
        ),
        migrations.CreateModel(
            name='TipoOrgano',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Código')),
                ('nombre', models.CharField(max_length=255, verbose_name='Órgano Jurisdiccional')),
                ('prioridad', models.IntegerField(blank=True, default=0, null=True, verbose_name='Prioridad')),
                ('abreviatura', models.CharField(max_length=10, verbose_name='Órgano Jurisdiccional')),
                ('nivel', models.IntegerField(blank=True, default=1, null=True, verbose_name='Prioridad')),
                ('tipo', models.CharField(choices=[('A', 'ADMINISTRATIVO'), ('J', 'JURISDICCIONAL')], default='J', max_length=5, verbose_name='Tipo')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
            ],
            options={
                'verbose_name': 'Órgano Jurisidiccional',
                'verbose_name_plural': 'Órganos Jurisidiccionales',
            },
        ),
        migrations.CreateModel(
            name='SedeJudicial',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Código Sede Judicial')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de la Sede Judicial')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('sede_corte', models.CharField(blank=True, max_length=10, null=True, verbose_name='Sede Central')),
                ('direccion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('latitud', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Latitud')),
                ('longitud', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Longitud')),
                ('provincia', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Provincia')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departments.distritojudicial')),
            ],
            options={
                'verbose_name': 'Sede Judicial',
                'verbose_name_plural': 'Sedes Judiciales',
            },
        ),
        migrations.CreateModel(
            name='EdificioInstitucional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Edificio Institucional', max_length=255, verbose_name='Edificio Institucional')),
                ('direccion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.distritojudicial')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.sedejudicial')),
            ],
            options={
                'verbose_name': 'Edificio Institucional',
                'verbose_name_plural': 'Edificios Institucionales',
            },
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Código')),
                ('nombre', models.CharField(max_length=255, verbose_name='Dependencia')),
                ('abreviatura', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Abreviatura')),
                ('condicion', models.CharField(choices=[('P', 'Permanente'), ('T', 'Transitorio')], default='P', max_length=5, verbose_name='Condición')),
                ('direccion', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Dirección')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departments.distritojudicial')),
                ('edificio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='departments.edificioinstitucional')),
                ('modulo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='departments.modulocoordinacion')),
                ('organo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departments.tipoorgano')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departments.sedejudicial')),
            ],
            options={
                'verbose_name': 'Dependencia',
                'verbose_name_plural': 'Dependencias',
            },
        ),
    ]
