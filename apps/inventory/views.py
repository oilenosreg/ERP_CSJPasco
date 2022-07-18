from audioop import reverse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

# App modules.
from .models import Equipo
from .forms import CreateEquipmentForm, AsignarEquipoForm


def list_equipos(request):
    equipos = Equipo.objects.all()

    template = 'inventory/list_equipos.html'
    context = { 
        'object_list': equipos,
        'pre_title': 'Parque Informático',
        'title': 'Registrar nuevo equipo',
    }
    return render(request, template, context)


# TODO:   Mejorar la tabla de los equipos y sus componentes.
#         ¿se debería usar un foreign key?
# Procesador 	Advance 	802 	Computadora Portátil Epson 2201-61063-001 - Sn: #789**** - 7879787897 	SN:qqqqqqqqq 	7879787897 	Inoperativo 	Bueno 
def create_equipo(request):
    if request.method == 'POST':
        form = CreateEquipmentForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request, 
                'Equipo registrado con éxito.')               
            return redirect('inventory:list_equipos')
        else:
            messages.error(
                request,
                'No fue posible guardar los datos. Verifique la información \
                ingresada.')
    else:
        form = CreateEquipmentForm()    
    template = 'inventory/create_equipo.html'
    context = { 
        'form': form,
        'create': True,
        'pre_title': 'Parque Informático',
        'title': 'Registrar nuevo equipo',
    }
    return render(request, template, context)


def edit_equipo(request, id):
    equipo = get_object_or_404(Equipo, id = id)
    form = CreateEquipmentForm(request.POST or None, instance=equipo)

    if form.is_valid():
        form.save()

        messages.success(
            request, 
            'Equipo modificado con éxito.')     

        return redirect('inventory:list_equipos')
    else:
        messages.error(
            request,
            '''
            No fue posible guardar los datos. Verifique la información \
            ingresada.
            ''')
    template = 'inventory/create_equipo.html'
    context = { 
        'form': form,
        'edit': True,
        'pre_title': 'Parque Informático',
        'title': 'Modificar equipo',
    }    
    return render(request, template, context)


def detail_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)

    template = 'inventory/detail_equipo.html'
    context = { 
        'equipo': equipo,
        'pre_title': 'Parque informático',
        'title': f'Detalle del equipo {equipo.categoria.nombre} {equipo.marca.nombre} {equipo.modelo.nombre} {equipo.serie}',
        'detail': True,
    }
    return render(request, template, context)


def asignar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id = id)
    if request.method == 'POST':
        form = AsignarEquipoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.equipo = equipo
            f.save()

            nombres = f.empleado.persona.nombres
            a_paterno = f.empleado.persona.apellido_paterno
            a_materno = f.empleado.persona.apellido_materno
            
            messages.success(
                request, 
                f'Equipo asignado a {nombres} {a_paterno} {a_materno} con éxito.')               
            return reverse_lazy('inventory:list_equipos')
        else:
            messages.error(
                request,
                'No fue posible guardar los datos. Verifique la información \
                ingresada.')

            # return redirect('inventory:asignar') # TODO: verificar si esto es correto.
    else:
        form = AsignarEquipoForm()
    # template = 'inventory/asignar_equipo.html'
    template = 'inventory/modal_asignar_equipo.html'
    context = {
        'form': form,
        'equipo': equipo,
        'pre_title': 'Parque informático',
        'title': 'Asignar equipo informático',
    }
    return render(request, template, context)