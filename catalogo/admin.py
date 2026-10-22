from django.utils.html import format_html
from django.contrib import admin
from .models import Catalogo, Categoria
# Register your models here.
admin.site.site_header = "Administración de la Tienda Tecnológica"


@admin.display(description="Precio", ordering="precio")
def precio(obj):
    return f"$ {obj.precio:,.0f}".replace(",", ".")


@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', precio, 'fecha_creacion', 'miniatura')
    readonly_fields = ('id', 'vista_previa_miniatura')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion',)
    ordering = ('-fecha_creacion',)

    @admin.display(description="Vista previa")
    def vista_previa_miniatura(self, obj):
        if obj and obj.miniatura:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px;">',
                obj.miniatura.url,
            )
        return "No hay imagen disponible"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'foreign_key')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('foreign_key',)
    ordering = ('nombre',)
