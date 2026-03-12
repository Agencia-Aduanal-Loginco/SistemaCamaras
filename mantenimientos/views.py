from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MantenimientoForm
from .models import Mantenimiento


@login_required
def lista_mantenimientos(request):
    """Lista todos los mantenimientos ordenados por fecha descendente."""
    mantenimientos = Mantenimiento.objects.select_related('camara').all()
    return render(request, 'mantenimientos/lista_mantenimientos.html', {
        'mantenimientos': mantenimientos,
    })


@login_required
def registrar_mantenimiento(request):
    """Registra un nuevo mantenimiento. GET muestra el formulario, POST lo guarda."""
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mantenimiento registrado correctamente.')
            return redirect('lista_mantenimientos')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = MantenimientoForm()

    return render(request, 'mantenimientos/registrar_mantenimiento.html', {
        'form': form,
    })


@login_required
def editar_mantenimiento(request, pk: int):
    """Edita un mantenimiento existente. GET muestra el formulario prellenado, POST guarda los cambios."""
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)

    if request.method == 'POST':
        form = MantenimientoForm(request.POST, instance=mantenimiento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mantenimiento actualizado correctamente.')
            return redirect('lista_mantenimientos')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = MantenimientoForm(instance=mantenimiento)

    return render(request, 'mantenimientos/editar_mantenimiento.html', {
        'form': form,
        'mantenimiento': mantenimiento,
    })


@login_required
def eliminar_mantenimiento(request, pk: int):
    """GET muestra confirmación de eliminación. POST elimina el registro."""
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)

    if request.method == 'POST':
        mantenimiento.delete()
        messages.success(request, 'Mantenimiento eliminado correctamente.')
        return redirect('lista_mantenimientos')

    return render(request, 'mantenimientos/eliminar_mantenimiento.html', {
        'mantenimiento': mantenimiento,
    })
