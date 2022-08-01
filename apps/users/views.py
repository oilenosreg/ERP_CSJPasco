from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect, get_list_or_404
from django.db.models import Q
from django.contrib import messages
from django.views import View

# Project modules.
from apps.employees.models import Empleado
from apps.persons.models import Persona

# App modules.
from .models import CustomUser
from .forms import CreateUserForm


def home(request):
    return render(request, 'usuarios/home.html')


def search_user_view(request):
    dni = request.GET.get('dni')
    if dni:
        try:
            persons = Persona.objects.filter(
                Q(dni__icontains = dni)
            )
        except Persona.DoesNotExist:
            messages.error(
                request, 
                f'No se encontraron personas con el número de DNI ingresado.'
            )
        except Persona.MultipleObjectsReturned:
            messages.error(
                request,
                f'Se han encontrado varias personas con el número de DNI ingresado.'
            )



class ListUsersView(ListView):
    model = CustomUser
    template_name = 'users/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pre_title'] = 'Administración de usuarios'
        context['title'] = 'Nuevo usuario'
        return context


class CreateUserView(View):    
    form_class = CreateUserForm
    initial = {'key': 'value'}
    template_name = 'users/modal_create.html'

    def get(self, request, *args, **kwargs):
        '''
        Si la petición is get, entonces crea un formulario vacío.
        '''
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        '''
        Si la petición is post, entonces crea una nueva instancia del formulario.        
        '''
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            dni = form.cleaned_data.get('dni')

            messages.success(
                request,
                f'Registro del usuario {dni} de manera exitosa.')
            # TODO: Aquí debe redirigir al formulario para registrar sus datos personales
            #       y datos de empleado.
            return redirect('usuarios:home')
        else:
            messages.error(
                request,
                f'No fue posible guardar los datos. Verifique la información ingresada.'
            )
        context = {'form': form}
        return render(request, self.template_name, context)


def create_user(request, dni):
    empleado = Empleado.objects.filter(persona=dni).first()
    persona = get_object_or_404(Persona, dni=dni)

    if empleado:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                f_u = form.save(commit=False)
                f_u.dni = persona.dni
                f_u.save()
                
                dni = form.cleaned_data.get('dni')

                messages.success(
                    request,
                    f'Registro del usuario {dni} de manera exitosa.')                
                return redirect('users:list')

            else:
                messages.error(
                    request,
                    f'No fue posible guardar los datos. Verifique la información ingresada.'
                )
        else:
            form = CreateUserForm()
        
    template = 'users/modal_create.html'
    context = {        
        'form': form,
        'persona': persona,
        'empleado': empleado,
        'pre_title': 'Administración de usuarios',
        'title': 'Nuevo usuario',
    }
    return render(request, template, context)
