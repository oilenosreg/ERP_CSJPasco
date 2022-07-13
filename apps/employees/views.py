from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

# Project modules.
from apps.departments.models import DistritoJudicial
from apps.persons.models import Persona
from django.conf import settings

# App modules.
from .models import Empleado
from .forms import CreateEmpleadoForm


def list_empleados(request):    
    empleados = Empleado.objects.select_related(
        'persona').filter(activo=True)

    template = 'employees/list.html'
    context = {
        'object_list': empleados,
        'pre_title': 'Empleados',
        'title': 'Lista de empleados',        
    }
    return render(request, template, context)


def create_empleado(request, dni):
    persona = get_object_or_404(Persona, dni = dni)
    DISTRITO = settings.DISTRITO
    distrito = get_object_or_404(DistritoJudicial, codigo = DISTRITO)

    if request.method == 'POST':
        form = CreateEmpleadoForm(request.POST)
        if form.is_valid():
            pt = form.save(commit=False)  
            pt.distrito = distrito
            pt.persona = persona
            pt.cargo = form.cleaned_data.get('cargo')
            pt.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CreateEmpleadoForm()
    
    # Historial de cargos.
    cargos = Empleado.objects.filter(persona = dni).order_by('-fecha_registro')

    # Paginación.
    # try:
    #     pagina = request.GET.get('pagina', 1)
    #     paginator = Paginator(cargos, 5)
    #     cargos = paginator.get_page(pagina)
    # except PageNotAnInteger:
    #     cargos = paginator.get_page(1)
    # except EmptyPage:
    #     cargos = paginator.get_page(paginator.num_pages)
    # except Http404:
    #     return Http404()

    template = 'employees/create.html'
    context = { 
        'form': form,
        'persona': persona,
        'distrito': distrito,
        'edit': True,
        'pre_title': 'Empleados',
        'title': 'Listado de empleados',
        
    }
    return render(request, template, context)


def edit_empleado(request,dni, id):
    DISTRITO = settings.DISTRITO
    distrito = get_object_or_404(DistritoJudicial, codigo = DISTRITO)
    persona = get_object_or_404(Persona, dni = dni)
    empleado = get_object_or_404(Empleado, id = id)
    cargos = Empleado.objects.filter(persona = dni).order_by('-fecha_registro')

    if request.method == 'POST':
        form = CreateEmpleadoForm(
            request.POST or None,            
            instance=empleado
        )
        if form.is_valid():
            form.save()
            # f_persona = form_persona.save(commit=False)
            # f_persona.save()
            # f_empleado = form.save(commit=False)
            # f_empleado.persona = f_persona
            # f_empleado.save()
            messages.success(request, 'Datos actualizados de manera correcta.')

            # TODO [0003]:  Definir a dónde debe retornar después de guardar
            #               correctamente los cambios.

            # TODO [0004]:  Mostrar la tabla de cargos que se detallan en el 
            #               empleado/nuevo_empleado/nuevo.html

            # TODO [0005]:  Dropdowns encadenados en el puesto de trabajo.
            # TODO [0006]:  Datos actualizados de manera correcta 3.
            # return('empleados:listar')

            # return HttpResponseRedirect('/empleados/nuevo/%s/'%empleado.persona.dni)
            
    else:
        # form_persona = PersonaForm(instance=persona)
        form = CreateEmpleadoForm(instance=empleado) 
    
    # plantilla = 'empleado/nuevo_empleado/nuevo.html'
    template = 'employees/create.html'
    context = {        
        'form': form,
        'object_list': cargos,
        'persona': persona,
        'editar': True,
        'pre_title': 'Empleados',
        'title': 'Modificación de datos del empleado',
    }
    return render(request, template, context)    