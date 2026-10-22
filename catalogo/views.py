from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Catalogo


def inicio(request):
    productos = Catalogo.objects.prefetch_related('categorias')

    cat = request.GET.get('categoria')
    if cat:
        productos = productos.filter(categorias__nombre=cat)

    q = request.GET.get('q')
    if q:
        productos = productos.filter(nombre__icontains=q)

    return render(request, "catalogo/inicio.html", {"productos": productos})

def detalle_producto(request, producto_nombre):
    try:
        producto = get_object_or_404(
            Catalogo.objects.prefetch_related("categorias"),
            nombre=producto_nombre,
        )
    except Http404:
        return render(request, "404.html", status=404)

    return render(request, "catalogo/detalle.html", {"producto": producto})
