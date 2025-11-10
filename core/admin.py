from django.contrib import admin
from .models import Familia, TipoAyuda, Voluntario, Entrega, Seguimiento

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'numero_integrantes')
    search_fields = ('nombre', 'direccion')

@admin.register(TipoAyuda)
class TipoAyudaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rol')

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('id', 'familia', 'tipo_ayuda', 'voluntario', 'fecha_entrega')
    list_filter = ('fecha_entrega', 'tipo_ayuda')

@admin.register(Seguimiento)
class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'familia', 'fecha')
    list_filter = ('fecha',)
