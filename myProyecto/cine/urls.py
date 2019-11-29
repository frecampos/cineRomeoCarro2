from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('formulario2/',formulario2,name='FORMU2'),
    path('quienes_somos/',quienessomos,name='QUIEN'),
    path('eliminar_pelicula/<id>/',eliminar_pelicula,name='ELIMINAR'),
    path('agregar_carro/<id>/',carro_compras,name='AGREGAR_CARRO'),
    path('login/',login,name='LOGIN'),
    path('cerrar_session/',cerrar_session,name='LOGOUT'),
    path('carro/',carros,name='CARRITO'),
    path('carro_mas/<id>/',carro_compras_mas,name='CARRO_MAS'),
    path('carro_menos/<id>/',carro_compras_menos,name='CARRO_MENOS'),
    path('grabar_carro/',grabar_carro,name='GRABAR_CARRO'),
]