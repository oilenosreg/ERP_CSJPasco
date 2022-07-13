#20 27 30 8 17 10

# =======================================================================
# TODO: [ ] Mejorar el algoritmo para cálculo de la edad de las personas.
# TODO: [ ] Tabla de listado de personas, columna acciones fija.
# TODO: [ ] Mejorar la interfaz de eliminación de usuarios.
# TODO: [ ] Pasar la vista de los títulos de las ventanas.
# TODO: [ ] Mejorar la interfaz cuando no haya registros en la base de
# TODO:     Datos.
# =======================================================================

from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.http import Http404, HttpRequest, HttpResponseRedirect
from django.urls import reverse

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
        'title': 'Lista de personas',

    }
    return render(request, plantilla, contexto)


def create_persona(request):
    '''
    Registra una persona en la base de datos.
    '''
    # TODO: Añadir un botón para agregar datos de empleado.

    if request.method == 'POST':
        form = CreatePersonaForm(request.POST, request.FILES)
        
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()    
            
            dni = persona.dni
            name = form.cleaned_data.get('nombres')
            f_lname = form.cleaned_data.get('apellido_paterno')
            m_lname = form.cleaned_data.get('apellido_materno')

            messages.success(
                request, 
                f'''
                Se ha registrado a {name} {f_lname} {m_lname} de {dni}
                manera correcta. ''')     

            if 'another' in request.POST:
                return HttpResponseRedirect(reverse('persons:create'))
            elif 'save' in request.POST:
                 return HttpResponseRedirect(reverse('persons:list'))
            elif 'department' in request.POST:
                return HttpResponseRedirect(
                    reverse('employees:create',
                        kwargs={'dni':dni}))
 

            # TODO [0002]:  Validar que el dni y puesto no sean NONE para evitar
            # TODO: return redirect('empleados:editar', dni=dni, id=puesto)

        else:
            messages.error(
                request,
                '''
                No fue posible guardar los datos. Verifique la información 
                ingresada.
                ''')
    else:
        form = CreatePersonaForm()
                
    template = 'persons/create.html'

    context = { 
        'form_persona': form,        
        'create': True,
        'pre_title': 'Personas',
        'title': 'Registrar nueva persona'
    }
    return render(request, template, context)       


def edit_persona(request, dni):
    persona = get_object_or_404(Persona, dni = dni)
    
    if request.method == 'POST':
        form = CreatePersonaForm(
            request.POST or None, 
            request.FILES or None,
            instance=persona
        )
        if form.is_valid():
            form.save()

            nombres = form.cleaned_data.get('nombres')
            f_lname = form.cleaned_data.get('apellido_paterno')
            m_lname = form.cleaned_data.get('apellido_materno')

            messages.success(
                request,
                f'''
                Datos de {nombres} {f_lname} {m_lname} actualizados con éxito.
                ''')

            if 'another' in request.POST:
                return HttpResponseRedirect(reverse('persons:create'))
            elif 'save' in request.POST:
                return HttpResponseRedirect(reverse('persons:list'))
        else:
            messages.error(
                request,
                '''
                No fue posible guardar los datos. Verifique la información 
                ingresada.
                ''')

    else:
        form = CreatePersonaForm(instance=persona)
            
    template = 'persons/create.html' 

    context = { 
        'persona': persona,
        'form_persona': form,
        'edit': True,
        'pre_title': 'Modificación de datos',
        'title': f'{persona.nombres} {persona.apellido_paterno} {persona.apellido_materno}'
    }
       
    return render(request, template, context)


def profile_persona(request, dni):
    persona = get_object_or_404(Persona, dni = dni)
    template = 'persons/profile.html'
    context = { 
        'persona': persona,        
        'detail': True,
        'pre_title': 'Personas',
        'title': 'Perfil de la persona'
        # 'title': f'{persona.nombres} {persona.apellido_paterno} {persona.apellido_materno}',
    }
    return render(request, template, context)