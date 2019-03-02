from django.shortcuts import render

# Create your views here.

def pagina_inicio(request):
    return render(request, 'index.html')


def pagina_sobre_mi(request):
    return render(request, 'sobre-mi.html')


def pagina_servicios(request):
    return render(request, 'servicios.html')


def pagina_contacto(request):
    return render(request, 'contacto.html')
