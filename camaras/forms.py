from django import forms
from .models import Camara

class CamaraForm(forms.ModelForm):
    class Meta:
        model = Camara
        fields = ['empresa', 'nombre', 'modelo', 'serie', 'ip', 'mac']