from django.db import models


from apps.persons.models import Persona
from apps.employees.models import Empleado


class Categoria(models.Model):
    # Foreign keys.
    subcategoria_de = models.ForeignKey('self', on_delete=models.PROTECT)

    # Datos de la categoría.
    nombre = models.CharField('Categoría', max_length=200, unique=True)    
    componentes = models.BooleanField('Componentes', default=False, help_text='¿Esta categoría almacenará a componentes, partes o piezas de otro equipo?')

    # Datos adicionales.
    observaciones = models.TextField('Observaciones', null=True, blank=True)    
    activo = models.BooleanField('Activo', default=True)

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)       

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class SubCategoria(models.Model):
    # Foreign keys.
    # categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    # Datos de la subcategoría.
    nombre = models.CharField('Categoría', max_length=200, unique=True)

    # Datos adicionales.
    observaciones = models.TextField('Observaciones', null=True, blank=True)    
    activo = models.BooleanField('Activo', default=True)

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)   

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Sub categoría'
        verbose_name_plural = 'Sub categorías'        


class Marca(models.Model):    
    # Datos de la marca.
    nombre = models.CharField('Nombre', max_length=50)

    # Datos adicionales.
    observaciones = models.TextField('Observaciones', null=True, blank=True)    
    activo = models.BooleanField('Activo', default=True)

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)       

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Modelo(models.Model):
    # Foreign keys.
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='marca')  

    # Datos del modelo.
    nombre = models.CharField('Nombre', max_length=50)   

    # Datos adicionales.
    observaciones = models.TextField('Observaciones', null=True, blank=True)    
    activo = models.BooleanField('Activo', default=True)  

    # Auditoría.
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última modificación', auto_now=True)    
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'


# Equipos.
CONDICION_CHOICES = ([
    ('B', 'Bueno'),
    ('R', 'Regular'),
    ('M', 'Malo'),])

ESTADO_CHOICES = ([
    ('O', 'Operativo'),
    ('I', 'Inoperativo'),
    ('N', 'Nuevo'),
    ('B', 'Baja'),])
class Equipo(models.Model):
    # empleado = models.ManyToManyField(Empleado, through='AsignarEquipo',related_name='empleado')
    # empleado = models.ManyToManyField(Empleado, through='AsignarEquipo',related_name='empleado')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)    
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    componente_de = models.ForeignKey('self', max_length=250, null=True, blank=True, on_delete=models.PROTECT)    
    serie = models.CharField('Número de Serie', max_length=200, null=True, blank=True)
    estado = models.CharField('Estado', max_length=5, choices=ESTADO_CHOICES, default='N')
    condicion = models.CharField('Condición', max_length=5, choices=CONDICION_CHOICES, default='B')
    asignado = models.BooleanField('Asignado', default=False)
    cod_patrimonial = models.CharField('Código Patrimonial', max_length=200, null=True, blank=True)
    ip = models.CharField('Dirección IP', max_length=200, null=True, blank=True)
    mac = models.CharField('Dirección MAC', max_length=200, null=True, blank=True)    
    orden_compra = models.CharField('Órden de Compra', max_length=200, null=True, blank=True)

    observaciones = models.TextField('Observaciones', max_length=255, blank=True, null=True)
    fecha_registro = models.DateTimeField('Fecha de Registro', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Última Modificación', auto_now=True)

    def __str__(self):
        return f'{self.categoria} {self.marca} {self.modelo} - {self.serie} - {self.cod_patrimonial}'

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'


ASIGNADO_CHOICES = ([
    ('V', 'VIGENTE'),
    ('A', 'ASIGNADO'),
    ('H', 'HISTÓRICO'),])
class EquipoAsignado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, related_name='ae_empleado')
    #dni = models.ForeignKey(Empleado, on_delete=models.PROTECT, related_name='puesto_trabajo')
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT, related_name='ae_equipo')
    inicio = models.DateTimeField('Inicio', null=False, blank=False, auto_now_add=True)
    fin = models.DateTimeField('Fin', null=True, blank=True, )
    asignado = models.TextField(choices=ASIGNADO_CHOICES, default='V')

    class Meta:
        verbose_name = 'Asignación de equipos'
        verbose_name_plural = 'Asignación de equipos'




# Especificaciones Técnicas de los equipos.
'''
TIPO_MONITOR_CHOICES = sorted([
    ('CRT', 'CRT'),
    ('LED', 'LED'),
    ('OLED', 'OLED'),
    ('PLASMA', 'PLASMA'),
    ('IPS', 'IPS'),
])

CONECTIVIDAD_CHOICES = sorted([
    ('HDMI', 'HDMI'),
    ('DP', 'Display Port'),
    ('VGA', 'VGA'),
    ('USB', 'USB'),    
    ('BT', 'Bluetooth'),
    ('PS2', 'PS/2'),
    ('LPT', 'LPT'),
    ('WIFI', 'WiFi')
])

TIPO_IMPRESORA_CHOICES = sorted([
    ('MULTI', 'MULTIFUNCIONAL'),
    ('MONO', 'MONOFUNCIONAL'),
])

TECNOLOGIA_IMPRESORA_CHOICES = sorted([
    ('LASER', 'Laser'),
    ('TINTA', 'Inyección de tinta'),
    ('MATRI', 'Matricial'),
    ('CARD', 'Tarjetas de PVC'),
    ('ETIQUETA', 'Etiquetas'),
])

COLORES_IMPRESORA_CHOICES = sorted([
    ('BN', 'Blanco y Negro'),
    ('COLOR', 'Colores'),
])


class Caracteristicas(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)

    # General
    conectividad_monitor = models.CharField(
        'Conectividad', max_length=200, 
        choices=CONECTIVIDAD_CHOICES, 
        default='USB'
    )

    # CPU.
    
    procesador = models.CharField('Procesador', max_length=200, null=True, blank=True)
    memoria = models.CharField('Memoria RAM', max_length=200, null=True, blank=True)
    almacenamiento = models.IntegerField('Disco Duro', null=True, blank=True)
    sistema_operativo = models.CharField('Memoria RAM', max_length=200, null=True, blank=True)


    # Monitor.
    tipo_monitor = models.CharField(
        'Tipo', max_length=200, 
        choices=TIPO_MONITOR_CHOICES, default='IPS'
    )
    tamaño = models.CharField(
        'Tamaño de Panel', max_length=200, 
        null=True, blank=True
    )
    resolucion = models.CharField(
        'Resolución', max_length=200, 
        null=True, blank=True
    )

    # Impresora
    tipo_impresora = models.CharField(
        'Tipo de impresora',
        choices=TIPO_IMPRESORA_CHOICES,
        default='MONO'
    )
    tecnologia_impresora = models.CharField(
        'Tecnología de impresión', max_length=200, 
        choices=TECNOLOGIA_IMPRESORA_CHOICES, 
        default='LASER',
    )
    colores_impresora = models.CharField(
        'Colores', max_length=200,
        choices=COLORES_IMPRESORA_CHOICES,
        default='BN'
    )

    # Escáner


    def __str__(self):
        return f'{self.equipo} {self.caracteristica} {self.descripcion}'

    class Meta:
        verbose_name = 'Características Técnicas'
        verbose_name_plural = 'Características Técnicas'
'''