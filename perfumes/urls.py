from django.urls import path
from . import views

urlpatterns = [
    # Login/Logout
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Marcas
    path('marcas/', views.marca_lista, name='marca_lista'),
    path('marcas/nova/', views.marca_criar, name='marca_criar'),
    path('marcas/<int:pk>/editar/', views.marca_editar, name='marca_editar'),
    
    # Perfumes
    path('perfumes/', views.perfume_lista, name='perfume_lista'),
    path('perfumes/novo/', views.perfume_criar, name='perfume_criar'),
    path('perfumes/<int:pk>/editar/', views.perfume_editar, name='perfume_editar'),
    
    # Clientes
    path('clientes/', views.cliente_lista, name='cliente_lista'),
    path('clientes/novo/', views.cliente_criar, name='cliente_criar'),
    path('clientes/<int:pk>/editar/', views.cliente_editar, name='cliente_editar'),
    path('clientes/<int:pk>/', views.cliente_detalhe, name='cliente_detalhe'),
    
    # Vendas
    path('vendas/', views.venda_lista, name='venda_lista'),
    path('vendas/nova/', views.venda_criar, name='venda_criar'),
    path('vendas/<int:pk>/', views.venda_detalhe, name='venda_detalhe'),
    path('vendas/<int:pk>/status/', views.venda_editar_status, name='venda_editar_status'),
    path('vendas/<int:pk>/status-ajax/', views.venda_atualizar_status_ajax, name='venda_status_ajax'),
    path('vendas/<int:pk>/deletar/', views.venda_deletar, name='venda_deletar'),
]
