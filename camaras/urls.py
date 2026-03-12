from django.urls import path

from . import views

urlpatterns = [
    path('registrar/', views.registrar_camara, name='registrar_camara'),
    path('<int:pk>/editar/', views.editar_camara, name='editar_camara'),
    path('<int:pk>/eliminar/', views.eliminar_camara, name='eliminar_camara'),
    path('', views.lista_camaras, name='lista_camaras'),
]
