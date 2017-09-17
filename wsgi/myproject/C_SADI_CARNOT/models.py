# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ciec.models import Condominio, TipoMovimiento, Banco, TipoCuenta, Proveedore, Servicio


class Cuenta(models.Model):
    clabe = models.CharField(max_length=18)
    apoderado = models.CharField(max_length=60)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_saldo = models.DateField(blank=True, null=True)
    situacion = models.IntegerField(blank=True, null=True)
    banco = models.ForeignKey(Banco)
    condominio = models.ForeignKey(Condominio, related_name='condominosadi_cuenta_id')
    tipo_cuenta = models.ForeignKey(TipoCuenta)

    def __str__(self):
        return '%s %s %s' % (self.condominio, self.clabe, self.apoderado[:10])

    class Meta:
        managed = True
        db_table = 'sadi_cuenta'

class Condomino(models.Model):
    depto = models.CharField(max_length=15, blank=True, null=True)
    propietario = models.CharField(max_length=60, blank=True, null=True)
    poseedor = models.CharField(max_length=60, blank=True, null=True)
    ubicacion = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    fecha_escrituracion = models.DateField(blank=True, null=True)
    fecha_ultimo_deposito = models.DateField(blank=True, null=True)
    referencia = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    condominio = models.ForeignKey(Condominio, related_name='condominosadi_condominio_id')

    def __str__(self):
        return '%s %s' % (self.depto, self.poseedor)

    class Meta:
        managed = True
        db_table = 'sadi_condomino'
        ordering = ['depto']

class Movimiento(models.Model):
    cuenta = models.ForeignKey(Cuenta, related_name='condominniosadi_movimiento_cuenta_id')
    fecha = models.DateField(blank=True, null=True)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, blank=True, null=True, related_name='condominiosadi_movimiento_tipo_movimiento_id')
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    retiro = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    deposito = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    recibo = models.IntegerField(blank=False, null=True, default=0)
    condomino = models.ForeignKey(Condomino, related_name='condominiosadi_movimiento_condomino_id')
    proveedor = models.ForeignKey(Proveedore, related_name='condominniosadi_movimiento_proveedor_id')
    servicio = models.ForeignKey(Servicio, related_name='condominniosadi_movimiento_servicio_id')

    def __str__(self):
        return u'%d %s %d %s' % (self.id, self.fecha.strftime('%d/%m/%Y'), self.deposito, self.descripcion[:15])

    class Meta:
        managed = True
        db_table = 'sadi_movimiento'
        ordering = ['fecha']

class Auxiliar(models.Model):
    cuenta = models.ForeignKey(Cuenta, related_name='olimpo_auxiliar_cuenta_id')
    fecha = models.DateField(blank=True, null=True)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, blank=True, null=True, related_name='olimpo_auxiliar_tipo_movimiento_id')
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    retiro = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    deposito = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    recibo = models.IntegerField(blank=False, null=True, default=0)
    condomino = models.ForeignKey(Condomino, related_name='condominiosadi_auxiliar_condomino_id')
    proveedor = models.ForeignKey(Proveedore, related_name='condominniosadi_auxiliar_proveedor_id')
    servicio = models.ForeignKey(Servicio, related_name='condominniosadi_auxiliar_servicio_id')

    def __str__(self):
        return u'%d %s %d %s' % (self.id, self.fecha.strftime('%d/%m/%Y'), self.deposito, self.descripcion[:15])

    class Meta:
        managed = True
        db_table = 'sadi_auxiliar'
        ordering = ['fecha']
