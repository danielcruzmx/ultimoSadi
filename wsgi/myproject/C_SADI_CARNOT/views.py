# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from ciec.utils import dictfetchall

class FaltantesMesViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valor = kw['mes_anio']
        #print valor
        query = '''
                SELECT  nombre as CONDOMINIO,
                        '%s' as MES,
                        concat(ubicacion,' ',depto) as DEPTO,
                        propietario AS CONDOMINO,
                        email as CORREO,
                        telefono as TELEFONO
                FROM sadi_condomino,
                     condominio
                WHERE sadi_condomino.condominio_id = condominio.id
                      and depto NOT IN
                     (SELECT depto
                            FROM sadi_movimiento,
                                 sadi_cuenta,
                                 sadi_condomino
                            WHERE sadi_movimiento.cuenta_id = sadi_cuenta.id
                            AND date_format(fecha,'%%m-%%Y') = '%s'
                            AND sadi_condomino.id = sadi_movimiento.condomino_id
                            AND sadi_condomino.depto != '0000'
                            AND deposito > 0)
                AND depto != '0000'       
                ORDER BY depto  ''' % (valor,valor)
        #print query
        cursor.execute(query)
        faltantes_list = dictfetchall(cursor)
        response = Response(faltantes_list, status=status.HTTP_200_OK)
        return response

class CuotasDeptoMesViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valor = kw['mes_anio']
        #print valor
        query = '''
                SELECT '%s' as MES,
                       nombre as CONDOMINIO,
                       depto as DEPTO,
                       propietario as PROPIETARIO,
                       sum(deposito) as DEPOSITO
                FROM sadi_movimiento, sadi_cuenta, sadi_condomino, condominio
                WHERE sadi_movimiento.cuenta_id = sadi_cuenta.id
                      and date_format(fecha,'%%m-%%Y') = '%s'
                      and sadi_condomino.id = sadi_movimiento.condomino_id
                      and sadi_condomino.depto != '0000'
                      and deposito > 0
                GROUP by 1,2,3,4
                UNION
                SELECT '%s' as MES,
                       nombre as CONDOMINIO,
                       depto as DEPTO,
                       propietario AS PROPIETARIO,
                       0 AS DEPOSITO
                FROM sadi_condomino, condominio
                WHERE sadi_condomino.condominio_id = condominio.id
                      and depto NOT IN
                         (SELECT depto
                          FROM sadi_movimiento,
                               sadi_cuenta,
                               sadi_condomino
                          WHERE sadi_movimiento.cuenta_id = sadi_cuenta.id
                          AND sadi_condomino.id = sadi_movimiento.condomino_id
                          AND sadi_condomino.depto != '0000'
                          AND date_format(fecha,'%%m-%%Y') = '%s'
                          AND deposito > 0)
                 AND depto != '0000'       
                 ORDER BY depto
        ''' % (valor, valor, valor, valor)
        #print query
        cursor.execute(query)
        cuotas_list = dictfetchall(cursor)
        response = Response(cuotas_list, status=status.HTTP_200_OK)
        return response

class MovimientosViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valorIni = kw['fec_ini']
        valorFin = kw['fec_fin']
        #print valor
        query = '''
            SELECT sadi_movimiento.id as NUM,
                   fecha AS FECHA,
                   tipo_movimiento.descripcion AS TIPO,
                   sadi_movimiento.descripcion AS DESCRIPCION,
                   CONCAT(sadi_condomino.depto,' ', sadi_condomino.propietario) AS CONDOMINO,
                   retiro AS RETIRO,
                   deposito AS DEPOSITO,
                   saldo AS SALDO,
                   sadi_condomino.depto AS DEPTO,
                   proveedore.proveedor as PROVEEDOR,
	               servicio.descripcion as SERVICIO
            FROM sadi_movimiento,
                 tipo_movimiento,
                 sadi_condomino,
                 condominio,
                 proveedore,
                 servicio
            WHERE sadi_movimiento.tipo_movimiento_id = tipo_movimiento.id
                  AND sadi_movimiento.condomino_id = sadi_condomino.id
                  AND sadi_condomino.condominio_id = condominio.id
                  AND fecha >= '%s'
                  AND fecha <= '%s'
                  AND proveedore.id = sadi_movimiento.proveedor_id
                  AND servicio.id = sadi_movimiento.servicio_id
            ORDER BY 2,1
        ''' % (valorIni, valorFin)
        #print query
        cursor.execute(query)
        movimientos_list = dictfetchall(cursor)
        response = Response(movimientos_list, status=status.HTTP_200_OK)
        return response

class RecibosViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valorIni = kw['fec_ini']
        valorFin = kw['fec_fin']
        #print valor
        query = '''
            SELECT sadi_movimiento.id as num,
                   fecha AS fecha,
                   tipo_movimiento.descripcion AS tipo,
                   sadi_movimiento.descripcion AS descripcion,
                   CONCAT(sadi_condomino.depto,' ', sadi_condomino.propietario) AS condomino,
                   retiro,
                   deposito,
                   letras(deposito) as monto,
                   recibo,
                   sadi_condomino.depto,
                   proveedore.proveedor as proveedor,
	               servicio.descripcion as servicio
            FROM sadi_movimiento,
                 tipo_movimiento,
                 sadi_condomino,
                 condominio,
                 proveedore,
                 servicio
            WHERE sadi_movimiento.tipo_movimiento_id = tipo_movimiento.id
                  AND sadi_movimiento.condomino_id = sadi_condomino.id
                  AND sadi_condomino.condominio_id = condominio.id
                  AND fecha >= '%s'
                  AND fecha <= '%s'
                  AND deposito > 0
                  AND proveedore.id = sadi_movimiento.proveedor_id
                  AND servicio.id = sadi_movimiento.servicio_id
            ORDER BY 2,1  
        ''' % (valorIni, valorFin)
        #print query
        cursor.execute(query)
        movimientos_list = dictfetchall(cursor)
        response = Response(movimientos_list, status=status.HTTP_200_OK)
        return response


class NoIdentificadosViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valorIni = kw['fec_ini']
        valorFin = kw['fec_fin']
        #print valor
        query = '''
           SELECT nombre as CONDOMINIO,
                  clabe as CUENTA,
                  fecha AS FECHA,
                  descripcion AS DESCRIPCION,
                  deposito AS DEPOSITO
           FROM sadi_movimiento,
                sadi_cuenta,
                sadi_condomino,
                condominio
           WHERE sadi_movimiento.cuenta_id = sadi_cuenta.id
           AND FECHA >= '%s'
           AND FECHA <= '%s'
           AND sadi_condomino.id = sadi_movimiento.condomino_id
           AND sadi_condomino.depto = '0000'
           AND sadi_cuenta.condominio_id = condominio.id
           AND deposito > 0
           ORDER BY FECHA
        ''' % (valorIni, valorFin)
        #print query
        cursor.execute(query)
        movimientos_list = dictfetchall(cursor)
        response = Response(movimientos_list, status=status.HTTP_200_OK)
        return response

class TotalIngresosEgresosViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valorIni = kw['fec_ini']
        valorFin = kw['fec_fin']
        #print valor
        query = '''
           SELECT nombre AS CONDOMINIO,
                  clabe as CUENTA,
                  sadi_cuenta.saldo as SALDO,
                  MIN(sadi_movimiento.FECHA) AS FECHAINI,
                  MAX(sadi_movimiento.FECHA) AS FECHAFIN,
                  SUM(sadi_movimiento.RETIRO) AS RETIROS,
                  SUM(sadi_movimiento.deposito) AS DEPOSITOS,
                  sum(deposito) - sum(retiro) AS SALDO
           FROM sadi_movimiento,
                sadi_cuenta,
                condominio
           WHERE sadi_cuenta.id = sadi_movimiento.cuenta_id
           AND FECHA >= '%s'
           AND FECHA <= '%s'
           AND sadi_cuenta.condominio_id = condominio.id
           GROUP BY cuenta
        ''' % (valorIni, valorFin)
        #print query
        cursor.execute(query)
        totales_list = dictfetchall(cursor)
        response = Response(totales_list, status=status.HTTP_200_OK)
        return response