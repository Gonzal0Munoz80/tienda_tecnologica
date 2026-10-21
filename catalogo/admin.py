from django.contrib import admin
from .models import Catalogo, Categoria
# Register your models here.
admin.site.site_header = "Administración de la Tienda Tecnológica"


@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'fecha_creacion')
    readonly_fields = ('id',)
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion',)
    ordering = ('-fecha_creacion',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'foreign_key')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('foreign_key',)
    ordering = ('nombre',)