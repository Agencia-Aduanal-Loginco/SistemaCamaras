from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_camara, name='registrar_camara'),
    path('', views.lista_camaras, name='lista_camaras'),
]