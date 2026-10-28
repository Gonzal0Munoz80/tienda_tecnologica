from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VentasForm
from .models import Catalogo


def inicio(request):
    productos = Catalogo.objects.prefetch_related('categorias')

    cat = request.GET.get('categoria')
    if cat:
        productos = productos.filter(categorias__nombre=cat)

    q = request.GET.get('q')
    if q:
        productos = productos.filter(nombre__icontains=q)

    return render(request, 'catalogo/inicio.html', {'productos': productos})


def detalle_producto(request, producto_nombre):
    try:
        producto = get_object_or_404(
            Catalogo.objects.prefetch_related('categorias'),
            nombre=producto_nombre,
        )
    except Http404:
        return render(request, '404.html', status=404)

    return render(request, 'catalogo/detalle.html', {'producto': producto})


def reservar(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            messages.success(
                request,
                f'Reserva registrada para el {reserva.fecha} a nombre de {reserva.nombre}',
            )
            return redirect('ventas')
    else:
        form = VentasForm()

    return render(request, 'catalogo/ventas.html', {'form': form})