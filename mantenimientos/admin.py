from django.contrib import admin

from .models import Mantenimiento


@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = [
        'camara',
        'fecha_mantenimiento',
        'proxima_fecha',
        'limpieza_lente',
        'limpieza_interior',
        'verificacion_conector',
        'verificacion_alimentacion',
    ]
    list_filter = ['fecha_mantenimiento', 'camara__empresa']
    search_fields = ['camara__nombre', 'camara__empresa']
