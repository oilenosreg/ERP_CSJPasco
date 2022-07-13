# Django.
from django.db import models

# Project modules.
from apps.persons.models import Persona
from apps.departments.models import (
    DistritoJudicial, SedeJudicial, Dependencia,
    ModuloCoordinacion, EdificioInstitucional,
)


TIPO_CHOICES = sorted([
    ('A', 'ADMINISTRATIVO'),
    ('J', 'JURISDICCIONAL'),])

class Cargo(models.Model):
    # Datos del cargo.
    nombre = models.CharField('Cargo', max_length=255, blank=False, null=False)
    tipo = models.CharField('Tipo', max_length=5, blank=False, null=False, choices=TIPO_CHOICES, default='J')

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)    

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'


class Empleado(models.Model):
    # Foreign keys.
    distrito = models.ForeignKey(DistritoJudicial, on_delete=models.PROTECT, null=False, blank=False,)   
    sede = models.ForeignKey(SedeJudicial, on_delete=models.PROTECT, null=False, blank=False, default=1)  
    modulo = models.ForeignKey(ModuloCoordinacion, on_delete=models.PROTECT, null=True, blank=True, default=1)  
    edificio = models.ForeignKey(EdificioInstitucional, on_delete=models.PROTECT, null=True, blank=True, default=1)  
    dependencia = models.ForeignKey(Dependencia, on_delete=models.PROTECT, null=False, blank=False, )    
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, null=False, blank=False, )
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='persona')

    # Datos del empleado.
    escalafon = models.CharField('Escalafón', max_length=5, blank=True, null=True)
    remuneracion = models.DecimalField('Remuneración', max_digits=12, decimal_places=2, blank=True, null=True)
    inicio = models.DateField('Inicio', null=True, blank=True,)
    cese = models.DateField('Cese', null=True, blank=True,)
    documento_designacion = models.CharField('Documento de asignación', max_length=255, null=True, blank=True,)
    observaciones = models.TextField('Observaciones', null=True, blank=True)
    activo = models.BooleanField(default=True)

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True) 

    def __str__(self):
        return f'{self.persona} - {self.dependencia} - {self.sede}' # TODO: ver si se puede poner el nombre completo y el cargo.

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'