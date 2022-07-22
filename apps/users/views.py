from typing import List
from django.views.generic import ListView
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.views import View

# App modules.
from .models import CustomUser
from .forms import CreateUserForm


def home(request):
    return render(request, 'usuarios/home.html')


class ListUsersView(ListView):
    model = CustomUser
    template_name = 'users/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pre_title'] = 'Administración de usuarios'
        context['title'] = 'Nuevo usuarios'
        return context



class CreateUserView(View):
    form_class = CreateUserForm
    initial = {'key': 'value'}
    template_name = 'users/create.html'

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