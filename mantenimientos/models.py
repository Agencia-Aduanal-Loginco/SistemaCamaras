from django.db import models
from django.utils.translation import gettext_lazy as _

from camaras.models import Camara


class Mantenimiento(models.Model):
    camara = models.ForeignKey(
        Camara,
        on_delete=models.CASCADE,
        verbose_name=_('Cámara'),
        related_name='mantenimientos',
    )
    limpieza_lente = models.BooleanField(
        default=False,
        verbose_name=_('Limpieza de lente'),
    )
    limpieza_interior = models.BooleanField(
        default=False,
        verbose_name=_('Limpieza interior'),
    )
    verificacion_conector = models.BooleanField(
        default=False,
        verbose_name=_('Verificación de conector'),
    )
    verificacion_alimentacion = models.BooleanField(
        default=False,
        verbose_name=_('Verificación de alimentación'),
    )
    fecha_mantenimiento = models.DateField(
        verbose_name=_('Fecha de mantenimiento'),
    )
    proxima_fecha = models.DateField(
        verbose_name=_('Próxima fecha'),
    )
    observaciones = models.TextField(
        blank=True,
        verbose_name=_('Observaciones'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_mantenimiento']
        verbose_name = _('Mantenimiento')
        verbose_name_plural = _('Mantenimientos')

    def __str__(self) -> str:
        return f"{self.camara.nombre} - {self.fecha_mantenimiento}"
