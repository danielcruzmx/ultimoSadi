# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Situacion(models.Model):
    situacion = models.CharField(max_length=25)

    def __str__(self):
        return '%s' % (self.situacion)

    class Meta:
        managed = True
        db_table = 'situacion'

class Servicio(models.Model):
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return '%s' % (self.descripcion)

    class Meta:
        managed = True
        db_table = 'servicio'

class TipoMovimiento(models.Model):
    descripcion = models.CharField(max_length=25)

    def __str__(self):
        return '%s' % (self.descripcion)

    class Meta:
        managed = True
        db_table = 'tipo_movimiento'

class TipoCuenta(models.Model):
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.descripcion)

    class Meta:
        managed = True
        db_table = 'tipo_cuenta'

class TipoCuota(models.Model):
    tipo = models.CharField(max_length=20)
    monto_minimo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    monto_maximo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.tipo)

    class Meta:
        managed = True
        db_table = 'tipo_cuota'

class Banco(models.Model):
    clave = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.clave, self.descripcion)

    class Meta:
        managed = True
        db_table = 'banco'

# ENTIDADES COMUNES

class Condominio(models.Model):
    nombre = models.CharField(max_length=45)
    calle = models.CharField(max_length=45, blank=True, null=True)
    colonia = models.CharField(max_length=45, blank=True, null=True)
    delegacion = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    regimen = models.CharField(max_length=45, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    fecha_constitucion = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.nombre)

    def movimientos(self):
        return '<a href="/admin/Condominio_%s/movimiento/">Movimientos banco</a>' % str(self.nombre)

    def condominos(self):
        return '<a href="/admin/Condominio_%s/condomino/">Lista condominos</a>' % str(self.nombre)

    movimientos.allow_tags = True
    condominos.allow_tags = True

    class Meta:
        managed = True
        db_table = 'condominio'

class Proveedore(models.Model):
    proveedor =  models.CharField(max_length=60)
    domicilio =  models.CharField(max_length=100, blank=True, null=True)
    telefono =  models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    servicio = models.ManyToManyField(Servicio)

    def __str__(self):
        return '%s'  % (self.proveedor)

    class Meta:
        managed = True
        db_table = 'proveedore'

class Periodo(models.Model):
    condominio = models.ForeignKey(Condominio)
    fecha_inicial = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.condominio)

    class Meta:
        managed = True
        db_table = 'periodo'
