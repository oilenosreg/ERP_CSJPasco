from django.db import models

# Project apps.
from apps.main.modules.images import renombrar_imagen


GENERO_CHOICES = sorted([
    ('MAS', 'MASCULINO'),
    ('FEM', 'FEMENINO'),
])

ESTADO_CIVIL_CHOICES = sorted([
    ('SOL', 'SOLTERO'),
    ('CAS', 'CASADO'),
    ('DIV', 'DIVORCIADO'),
])    
class Persona(models.Model):    
    # Datos personales.
    dni = models.CharField('DNI', max_length=8, primary_key=True)
    nombres = models.CharField('Nombres', max_length=250)
    apellido_paterno = models.CharField('Apellido paterno', max_length=250)
    apellido_materno = models.CharField('Apellido materno', max_length=250)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=False, default=None)
    genero = models.CharField('Género', max_length=10, choices=GENERO_CHOICES, default='MAS')
    estado_civil = models.CharField('Estado civil', max_length=200, choices=ESTADO_CIVIL_CHOICES, default='SOL')
    foto = models.ImageField('Foto', upload_to=renombrar_imagen, null=True, blank=True)
    
    # # Datos de contacto.
    # correo_institucional = models.EmailField('Correo electrónico institucional', max_length=150, null=True, blank=True)
    # correo_personal = models.EmailField('Correo electrónico personal', max_length=200, blank=True, null=True)    
    # telefono_principal = models.CharField('Nro de Teléfono institucional', max_length=9, null=True, blank=True)
    # telefono_secundario = models.CharField('Nro de Teléfono personal', max_length=9, null=True, blank=True)
    # anexo_institucional = models.CharField('Anexo telefónico', max_length=10, null=True, blank=True)
    # direccion = models.CharField('Direccion', max_length=255, null=True, blank=True)        

    # Datos adicionales.
    observaciones = models.TextField('Observaciones', null=True, blank=True)    
    activo = models.BooleanField(default=True)    

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)

    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}' 

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
