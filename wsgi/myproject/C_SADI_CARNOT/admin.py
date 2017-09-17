# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Condomino, Movimiento, Auxiliar, Cuenta

class AuxiliarAdminA(admin.ModelAdmin):
	list_display = ('id','fecha','tipo_movimiento','retiro','deposito','condomino')
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

class MovimientoAdminB(admin.ModelAdmin):
	list_display = ('id','fecha','tipo_movimiento','retiro','deposito','condomino')
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

class CondominoAdminB(admin.ModelAdmin):
	list_display = ('depto','ubicacion','propietario','poseedor')
	search_fields = ('depto','propietario','poseedor')

class CuentaAdmin(admin.ModelAdmin):
    list_display = ('condominio','banco','clabe','apoderado')

admin.site.register(Movimiento, MovimientoAdminB)
admin.site.register(Auxiliar, AuxiliarAdminA)
admin.site.register(Condomino, CondominoAdminB)
admin.site.register(Cuenta, CuentaAdmin)