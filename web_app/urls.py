from django.urls import path
from web_app import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('servicios.html', views.pagina_servicios, name='pagina_servicios'),
    path('sobre-mi.html', views.pagina_sobre_mi, name='pagina_sobre-mi'),
    path('contacto.html', views.pagina_contacto, name='pagina_contacto')
]