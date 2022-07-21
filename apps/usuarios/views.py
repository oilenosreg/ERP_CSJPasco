from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.views import View

# App modules.
from .models import Usuario
from .forms import RegistroUsuarioForm


def home(request):
    return render(request, 'usuarios/home.html')


class RegistroUsuarioView(View):
    form_class = RegistroUsuarioForm
    initial = {'key': 'value'}
    template_name = 'usuarios/register.html'

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
            # return redirect()
        else:
            messages.error(
                request,
                f'No fue posible guardar los datos. Verifique la información ingresada.'
            )
        context = {'form': form}
        return render(request, self.template_name, context)