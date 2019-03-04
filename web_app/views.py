from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

def pagina_inicio(request):
    return render(request, 'index.html')


def pagina_sobre_mi(request):
    return render(request, 'sobre-mi.html')


def pagina_marketing_contenidos(request):
    return render(request, 'marketing-de-contenidos.html')


def pagina_valor_palabras(request):
    return render(request, 'valor-palabras.html')


def pagina_contacto(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        template = get_template('web_app/contact_template.txt')
        context = {'name': name, 'email': email, 'phone': phone, 'message': message}
        content = template.render(context)
        send_mail('Nuevo formulario de contacto', content, settings.DEFAULT_FROM_EMAIL, ['mgvaquera@gmail.com'],
                  fail_silently=True)
        return redirect('success.html')
    return render(request, 'contacto.html')


def pagina_success(request):
    return HttpResponse('El formulario se ha enviado con éxito')
