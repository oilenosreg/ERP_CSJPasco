from django.shortcuts import get_list_or_404, redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# Project modules.
from apps.departments.models import Dependencia, DistritoJudicial
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

# TODO: Crear mensaje de error cuando no existe distrito judicial.
def create_empleado(request, dni):
    persona = get_object_or_404(Persona, dni = dni)

    # Validación del Distrito Judicial.
    # try:
    DISTRITO = settings.DISTRITO
    # distrito = DistritoJudicial.objects.filter(codigo = DISTRITO)
    distrito = get_object_or_404(DistritoJudicial, codigo=DISTRITO)
    # except DistritoJudicial.DoesNotExist:
    #     distrito = None
    #     messages.error(
    #         request,
    #         f'No se ha registrado ningún Distrito Judicial en el sistema.'
    #     )
    # except DistritoJudicial.MultipleObjectsReturned:
    #     messages.error(
    #         request,
    #         f'Se han encontrado varios Distritos Judiciales con el mismo código.'
    #     )

    if request.method == 'POST':
        form = CreateEmpleadoForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)  
            employee.distrito = distrito
            employee.persona = persona
            employee.cargo = form.cleaned_data.get('cargo')
            employee.save()
            
            sede = employee.sede.nombre
            dependencia = employee.dependencia.nombre
            
            messages.success(
                request,
                f'Empleado registrado con éxito en "{dependencia}"')
            
            if 'user' in request.POST:
                return HttpResponseRedirect(reverse('users:create', kwargs={'dni': dni}))
            if 'save' in request.POST:
                return HttpResponseRedirect(reverse('employees:list'))
        else:
            messages.error(
                request,
                'No fue posible guardar los datos. Verifique la información \
                ingresada.')
    else:
        form = CreateEmpleadoForm()

    template = 'employees/create.html'
    context = { 
        'form': form,
        'persona': persona,
        'distrito': distrito,
        'edit': True,
        'pre_title': 'Empleados',
        'title': 'Registrar nuevo empleado',        
    }
    return render(request, template, context)


# TODO: No devuelve la fecha cuando se edita.
# TODO [0005]:  Dropdowns encadenados en el puesto de trabajo.
# TODO: Checkbox "Activo" estilos del dashboard.
def edit_empleado(request,dni, id):
    DISTRITO = settings.DISTRITO
    distrito = get_object_or_404(DistritoJudicial, codigo = DISTRITO)
    persona = get_object_or_404(Persona, dni = dni)
    empleado = get_object_or_404(Empleado, id = id)
    # cargos = Empleado.objects.filter(persona = dni).order_by('-fecha_registro')

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
            messages.success(
                request,
                'Datos del empleado actualizados de manera correcta.')
            return redirect('employees:list')
        else:
            messages.error(
                request,
                'No fue posible guardar los datos. Verifique la información \
                ingresada.')            
    else:
        form = CreateEmpleadoForm(instance=empleado) 
    
    template = 'employees/create.html'
    context = {        
        'form': form,
        'persona': persona,
        'editar': True,
        'pre_title': 'Empleados',
        'title': 'Modificación de datos del empleado',
    }
    return render(request, template, context)    


# TODO: El perfile debe pasar a la aplicación empleado.


def list_departments(request, dni):
    # empleado = get_list_or_404(Empleado, persona=dni)
    # try:
    employee = Empleado.objects.select_related('persona').filter(persona=dni)
    

    template = 'employees/employee_departments_list.html'
    context = {
        'object_list': employee,
        'pre_title': 'Dependencias',
        'title': 'Listado de cargos del empleado',        
    }
    return render(request, template, context)