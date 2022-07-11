#20 27 30 8 17 10

# =======================================================================
# TODO: [ ] Mejorar el algoritmo para cálculo de la edad de las personas.
# TODO: [ ] Tabla de listado de personas, columna acciones fija.
# TODO: [ ] Mejorar la interfaz de eliminación de usuarios.
# TODO: [ ] Pasar la vista de los títulos de las ventanas.
# TODO: [ ] Mejorar la interfaz cuando no haya registros en la base de
# TODO:     Datos.
# =======================================================================

from django.shortcuts import render
from django.db.models import Q

# App modules.
from .models import Persona
from .forms import CreatePersonaForm


def list_personas(request):
    '''
    Muestra un listado de las personas registradas en la base de datos, en condición
    Activo.
    '''
    # personas = Persona.objects.select_related('datoscontacto').all().order_by('apellido_paterno')  
    personas = Persona.objects.all().filter(activo=True).order_by('apellido_paterno')  
    #-ultima_modificacion
    consulta = request.GET.get('buscar')
    if consulta:
        # personas = Persona.objects.select_related('datoscontacto').filter(
        personas = Persona.objects.filter(
            Q(dni__icontains = consulta) |
            Q(nombres__icontains = consulta) |
            Q(apellido_paterno__icontains = consulta) |
            Q(apellido_materno__icontains = consulta) 
        ).order_by('apellido_paterno')

    plantilla = 'persons/list.html'
    contexto = {
        'personas' : personas,
        'pre_title': 'Personas',        
        'title': 'Listado de personas',

    }
    return render(request, plantilla, contexto)
