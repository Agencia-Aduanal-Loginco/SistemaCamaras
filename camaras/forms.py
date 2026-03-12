import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Camara

MAC_REGEX = re.compile(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$')


class CamaraForm(forms.ModelForm):
    class Meta:
        model = Camara
        fields = ['empresa', 'nombre', 'modelo', 'serie', 'ip', 'mac']

    def clean_mac(self) -> str:
        mac: str = self.cleaned_data.get('mac', '')
        if not MAC_REGEX.match(mac):
            raise ValidationError(
                'Formato de MAC inválido. Use el formato AA:BB:CC:DD:EE:FF'
            )
        return mac.upper()
