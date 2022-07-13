from django.db import models


class DistritoJudicial(models.Model):
    # Primary key.    
    codigo = models.CharField('Código', max_length=50, primary_key=True)

    # Datos del Distrito Judicial.
    nombre = models.CharField('Nombre', max_length=200)
    ubigeo = models.CharField('Ubigeo', max_length=10, default=None, null=True, blank=True)    
    latitud = models.CharField('Latitud', max_length=50, default=None, null=True, blank=True)
    longitud = models.CharField('Longitud', max_length=50, default=None, null=True, blank=True)
    ncpp = models.DateField('NCPP', default=None, null=True, blank=True)
    nlpt = models.DateField('NLPT', default=None, null=True, blank=True)
    corte = models.CharField('Corte', max_length=256, default=None, null=True, blank=True)

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta: 
        ordering = ['nombre']
        verbose_name = 'Distrito Judicial'
        verbose_name_plural = 'Distritos Judiciales'


class SedeJudicial(models.Model):  
    # Primary key.
    codigo = models.CharField('Código Sede Judicial', primary_key=True, max_length=10)    

    # Foreign key.
    distrito = models.ForeignKey(DistritoJudicial, on_delete=models.PROTECT) 

    # Datos de la Sede Judicial.
    nombre = models.CharField('Nombre de la Sede Judicial', max_length=200)
    activo = models.BooleanField('Activo', default=True)
    sede_corte = models.CharField('Sede Central', max_length=10, null=True, blank=True)
    direccion = models.CharField('Dirección', max_length=255, blank=True, null=True)
    latitud = models.CharField('Latitud', max_length=50, default=None, null=True, blank=True)
    longitud = models.CharField('Longitud', max_length=50, default=None, null=True, blank=True) 
    provincia = models.CharField('Provincia', max_length=10, default=None, null=True, blank=True) 
  
    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Sede Judicial'
        verbose_name_plural = 'Sedes Judiciales'


class EdificioInstitucional(models.Model):
    # Foreign key.
    distrito = models.ForeignKey(DistritoJudicial, on_delete=models.CASCADE)
    sede = models.ForeignKey(SedeJudicial, on_delete=models.CASCADE)

    # Datos del Edificio Institucional.
    nombre = models.CharField('Edificio Institucional', max_length=255, default='Edificio Institucional')
    direccion = models.CharField('Dirección', max_length=255, blank=True, null=True)

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Edificio Institucional'
        verbose_name_plural = 'Edificios Institucionales'


class ModuloCoordinacion(models.Model):
    nombre = models.CharField('Módulo o Coordinación', max_length=255)

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'    




# Órganos Jurisdiccionales y Administrativos.
TIPO_DEPENDENCIA_CHOICES = sorted([
    ('A', 'ADMINISTRATIVO'),
    ('J', 'JURISDICCIONAL'),])

class TipoOrgano(models.Model): 
    '''
    Tabla maestra: Define los tipos de órganos jurisdiccionales, su prioridad y
    nivel; también define el tipo de los órganos administrativos, ejemplo.
    órganos de dirección, órganos de líneas, entre otros.
    '''

    # Primary key.
    codigo = models.CharField('Código', primary_key=True, max_length=10)

    # Campos de la tabla.
    nombre = models.CharField('Órgano Jurisdiccional', max_length=255)
    prioridad = models.IntegerField('Prioridad', null=True, blank=True, default=0)
    abreviatura = models.CharField('Órgano Jurisdiccional', max_length=10)
    nivel = models.IntegerField('Prioridad', null=True, blank=True, default=1)
    tipo = models.CharField('Tipo', max_length=5, choices=TIPO_DEPENDENCIA_CHOICES, default='J',)
    activo = models.BooleanField('Activo', default=True)
  
    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Órgano Jurisidiccional'
        verbose_name_plural = 'Órganos Jurisidiccionales'


CONDICION_CHOICES = sorted([
    ('P', 'Permanente'),
    ('T', 'Transitorio'),])

class Dependencia(models.Model):
    # Primary key.
    codigo = models.CharField('Código', max_length=10, primary_key=True)  

    # Foreing keys.
    distrito = models.ForeignKey(DistritoJudicial, on_delete=models.PROTECT)
    sede = models.ForeignKey(SedeJudicial, on_delete=models.PROTECT)    
    organo = models.ForeignKey(TipoOrgano, on_delete=models.PROTECT)  
    modulo = models.ForeignKey(ModuloCoordinacion, on_delete=models.PROTECT, blank=True, null=True)
    edificio = models.ForeignKey(EdificioInstitucional, on_delete=models.PROTECT, blank=True, null=True)

    # Campos de la tabla.
    nombre = models.CharField('Dependencia', max_length=255)
    abreviatura = models.CharField('Abreviatura', max_length=10, default=None, null=True, blank=True)    
    condicion = models.CharField('Condición', max_length=5, choices=CONDICION_CHOICES, default='P')    
    direccion = models.CharField('Dirección', max_length=255, null=True, blank=True, default=None)
    activo = models.BooleanField('Activo', default=True)

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Dependencia'
        verbose_name_plural = 'Dependencias'
