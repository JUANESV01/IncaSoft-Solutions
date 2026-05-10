from django.contrib import admin

from .models import Auditoria, Colaborador, HistorialEstado, Incapacidad, TipoIncapacidad


@admin.register(TipoIncapacidad)
class TipoIncapacidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "entidad_responsable", "activo")
    search_fields = ("nombre", "codigo")
    list_filter = ("entidad_responsable", "activo")


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "numero_identificacion", "area", "cargo", "eps", "activo")
    search_fields = ("nombres", "apellidos", "numero_identificacion", "area")
    list_filter = ("area", "activo", "eps")
    readonly_fields = ("fecha_creacion", "fecha_actualizacion")


class HistorialEstadoInline(admin.TabularInline):
    model = HistorialEstado
    extra = 0
    readonly_fields = ("estado_anterior", "estado_nuevo", "comentario", "usuario", "fecha")
    can_delete = False


@admin.register(Incapacidad)
class IncapacidadAdmin(admin.ModelAdmin):
    list_display = ("colaborador", "tipo", "estado", "fecha_inicio", "fecha_fin", "dias", "entidad_responsable")
    search_fields = ("colaborador__nombres", "colaborador__apellidos", "colaborador__numero_identificacion", "numero_radicado")
    list_filter = ("estado", "tipo", "entidad_responsable")
    readonly_fields = ("dias", "fecha_creacion", "fecha_actualizacion")
    inlines = [HistorialEstadoInline]


@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ("accion", "usuario", "fecha")
    search_fields = ("accion", "detalle", "usuario__username")
    readonly_fields = ("usuario", "accion", "detalle", "fecha")

