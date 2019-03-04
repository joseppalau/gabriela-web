from django.urls import path
from web_app import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('marketing-de-contenidos.html', views.pagina_marketing_contenidos, name='pagina_marketing_contenidos'),
    path('sobre-mi.html', views.pagina_sobre_mi, name='pagina_sobre-mi'),
    path('valor-palabras.html', views.pagina_valor_palabras, name="pagina_valor_palabras"),
    path('contacto.html', views.pagina_contacto, name='pagina_contacto'),
    path('success.html', views.pagina_success, name='pagina_success')
]