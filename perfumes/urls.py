from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login',views.index, name='index'),

    path('menu',views.menu, name='menu'),
    
    #perfumes
    path('listagemperfumes',views.listagemperfumes,name='listagemperfumes'),
    path('deletar_perfume/<int:id>/',views.deletar_perfume,name='deletar_perfume'),

    #tamanhos
    path('listagemtamanhos',views.listagemtamanhos,name='listagemtamanhos'),
    path('deletar_tamanho/<int:id>/',views.deletar_tamanho,name='deletar_tamanho'),
    #tipos
    path('listagemtipos',views.listagemtipos,name='listagemtipos'),
    path('deletar_tipo/<int:id>/',views.deletar_tipo,name='deletar_tipo'),

    #fabricantes
    path('listagemfabricantes',views.listagemfabricantes,name='listagemfabricantes'),
    path('deletar_fabricante/<int:id>/',views.deletar_fabricante,name='deletar_fabricante'),
    
    #clientes
    path('listagemclientes',views.listagemclientes,name='listagemclientes'),
    path('deletar_cliente/<int:id>/',views.deletar_cliente,name='deletar_cliente'),

    #vendas
    path('listagemvendas',views.listagemvendas,name='listagemvendas'),
    path('deletar_venda/<int:id>/',views.deletar_venda,name='deletar_venda'),

    #dashboard
    path('dashboard',views.dashboard,name='dashboard'),

    #logoff
    path('sair',views.sair,name='sair'),
    
    #logout
    path('logoff',views.logoff,name='logoff')
    ]
