# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from utils import dictfetchall

#@login_required()
def home(request):
    return HttpResponseRedirect('/admin/ciec')

class ServiciosViewSet(APIView):

    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        query = '''
                Select descripcion
                From servicio
        '''
        #print query
        cursor.execute(query)
        cuotas_list = dictfetchall(cursor)
        response = Response(cuotas_list, status=status.HTTP_200_OK)
        return response
