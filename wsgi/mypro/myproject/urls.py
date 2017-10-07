"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ciec.views import ServiciosViewSet
from C_SADI_CARNOT.views import FaltantesMesViewSet, \
                                CuotasDeptoMesViewSet, \
                                MovimientosViewSet, \
                                NoIdentificadosViewSet, \
                                TotalIngresosEgresosViewSet, \
                                RecibosViewSet
from ciec.views import home

urlpatterns = [
    url(r'^$',
        home,
        name='home'),
    url(r'^api-rest/servicios/$',
        ServiciosViewSet.as_view(),
        name='my_rest_view'),
    url(r'^api-rest/faltantesMes/(?P<mes_anio>(0?[1-9]|1[012])-((19|20)\d\d))/$',
        FaltantesMesViewSet.as_view(),
        name='my_rest_view'),
    url(r'^api-rest/cuotasDeptoMes/(?P<mes_anio>(0?[1-9]|1[012])-((19|20)\d\d))/$',
        CuotasDeptoMesViewSet.as_view(),
        name='my_rest_view'),
    url(r'^api-rest/movimientos/(?P<fec_ini>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/$',
        MovimientosViewSet.as_view(),
        name='my_rest_view'),
    url(r'^api-rest/recibos/(?P<fec_ini>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/$',
        RecibosViewSet.as_view(),
        name='my_rest_view'),
    url(r'^api-rest/noIdentificados/(?P<fec_ini>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/$',
        NoIdentificadosViewSet.as_view(),
        name='my_rest_view'),
    url(r'^api-rest/totalIngresosEgresos/(?P<fec_ini>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/$',
        TotalIngresosEgresosViewSet.as_view(),
        name='my_rest_view'),
    url(r'^admin/', include(admin.site.urls)),
]
