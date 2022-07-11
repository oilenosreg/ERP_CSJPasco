from django.shortcuts import render


def index(request):
    template = 'main/index.html'
    context = {
        'pre_title': 'Prueba',
        'title': 'Página de inicio',
    }
    return render(request, template, context)
