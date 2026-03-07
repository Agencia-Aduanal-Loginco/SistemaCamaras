from django.shortcuts import render, redirect
from .forms import CamaraForm
from .models import Camara

def registrar_camara(request):
    if request.method == 'POST':
        form = CamaraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_camaras')
    else:
        form = CamaraForm()

    return render(request, 'registrar_camara.html', {'form': form})


def lista_camaras(request):
    camaras = Camara.objects.all()
    return render(request, 'lista_camaras.html', {'camaras': camaras})