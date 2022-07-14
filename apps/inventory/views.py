from django.shortcuts import render, redirect

# App modules.
from .models import Equipo
from .forms import CreateEquipmentForm


def list_equipos(request):
    equipos = Equipo.objects.all()

    template = 'inventory/list_equipos.html'
    context = { 
        'object_list': equipos,
        'pre_title': 'Parque Informático',
        'title': 'Registrar nuevo equipo',
    }
    return render(request, template, context)


def create_equipo(request):
    if request.method == 'POST':
        form = CreateEquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipo:listar')
    else:
        form = CreateEquipmentForm()    
    plantilla = 'inventory/create_equipo.html'
    contexto = { 
        'form': form,
        'create': True,
        'pre_title': 'Parque Informático',
        'title': 'Registrar nuevo equipo'
    }
    return render(request, plantilla, contexto)