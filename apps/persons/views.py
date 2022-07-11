#20 27 30 8 17 10

# =======================================================================
# TODO: [ ] Mejorar el algoritmo para cálculo de la edad de las personas.
# TODO: [ ] Tabla de listado de personas, columna acciones fija.
# TODO: [ ] Mejorar la interfaz de eliminación de usuarios.
# TODO: [ ] Pasar la vista de los títulos de las ventanas.
# TODO: [ ] Mejorar la interfaz cuando no haya registros en la base de
# TODO:     Datos.
# =======================================================================

from django.shortcuts import render, redirect, get_list_or_404
from django.db.models import Q
from django.contrib import messages
from django.http import Http404, HttpRequest

# Project modules.
from django.conf import settings

# App modules.
from .models import Persona
from .forms import CreatePersonaForm


def list_personas(request):
    '''
    Muestra un listado de las personas registradas en la base de datos, en condición
    Activo.
    '''
    # TODO: MOSTRAR UNA PÁGINA EN CASO NO HAYA REGISTROS.

    personas = Persona.objects.all().filter(activo=True).order_by('apellido_paterno')  
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


def create_persona(request):
    '''
    Registra una persona en la base de datos.
    '''

    if request.method == 'POST':
        create_form = CreatePersonaForm(request.POST, request.FILES)
        
        if create_form.is_valid():
            persona = create_form.save(commit=False)
            persona.save()    
            
            name = create_form.cleaned_data.get('nombres')
            f_lname = create_form.cleaned_data.get('apellido_paterno')
            m_lname = create_form.cleaned_data.get('apellido_materno')
            messages.success(
                request, 
                f'''
                Se ha registrado a {name} {f_lname} {m_lname} de 
                manera correcta. ''')        

            # TODO [0002]:  Validar que el dni y puesto no sean NONE para evitar
            # FIXME: prueba.
            # BUG: prueba.

            # return redirect('empleados:editar', dni=dni, id=puesto)
        else:
            messages.error(
                request,
                '''
                No fue posible guardar los datos, verifique la información 
                ingresada.
                ''')
    else:
        create_form = CreatePersonaForm()
        # form_empleado = EmpleadoForm()
        
    template = 'persons/create.html'

    context = { 
        'form_persona': create_form,
        # 'form_empleado': form_empleado,
        'create': True,
        'pre_title': 'Personas',
        'title': 'Registrar nueva persona'
    }
    return render(request, template, context)       
