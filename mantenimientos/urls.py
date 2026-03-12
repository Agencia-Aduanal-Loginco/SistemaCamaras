from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_mantenimientos, name='lista_mantenimientos'),
    path('registrar/', views.registrar_mantenimiento, name='registrar_mantenimiento'),
    path('<int:pk>/editar/', views.editar_mantenimiento, name='editar_mantenimiento'),
    path('<int:pk>/eliminar/', views.eliminar_mantenimiento, name='eliminar_mantenimiento'),
]
