# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Banco, TipoCuenta, Condominio, Proveedore, \
                   TipoCuota, TipoMovimiento, Situacion, Servicio, Periodo

# Register your models here.

class BancoAdmin(admin.ModelAdmin):
    list_display = ('clave','descripcion')

class TipoCuentaAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class SituacionAdmin(admin.ModelAdmin):
    list_display = ('situacion',)

class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class TipoCuotaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'monto_minimo', 'monto_maximo')

class CondominioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'condominos', 'movimientos')

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'rfc', 'domicilio')

class PeriodosAdmin(admin.ModelAdmin):
    list_display = ('condominio', 'fecha_inicial', 'fecha_final')


admin.site.register(Banco, BancoAdmin)
admin.site.register(TipoCuenta, TipoCuentaAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(TipoMovimiento, TipoMovimientoAdmin)
admin.site.register(Situacion, SituacionAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(TipoCuota, TipoCuotaAdmin)
admin.site.register(Proveedore, ProveedoresAdmin)
admin.site.register(Periodo, PeriodosAdmin)

