#!/usr/bin/env python
"""Script para popular o banco de dados com dados de exemplo"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gravaperfumes.settings')
django.setup()

from perfumes.models import Marca, Perfume, Cliente, Venda, ItemVenda
from decimal import Decimal

def popular():
    print("🚀 Populando banco de dados...")
    
    # Criar Marcas
    print("\n📦 Criando marcas...")
    marcas_data = [
        {'nome': 'Chanel', 'descricao': 'Marca francesa de luxo'},
        {'nome': 'Dior', 'descricao': 'Alta costura e perfumaria francesa'},
        {'nome': 'Versace', 'descricao': 'Marca italiana de moda e fragrâncias'},
        {'nome': 'Carolina Herrera', 'descricao': 'Elegância e sofisticação'},
        {'nome': 'Paco Rabanne', 'descricao': 'Fragrâncias modernas e ousadas'},
    ]
    
    marcas = {}
    for marca_data in marcas_data:
        marca, created = Marca.objects.get_or_create(
            nome=marca_data['nome'],
            defaults={'descricao': marca_data['descricao']}
        )
        marcas[marca.nome] = marca
        print(f"  ✓ {marca.nome}")
    
    # Criar Perfumes
    print("\n💐 Criando perfumes...")
    perfumes_data = [
        {'nome': 'Chanel N°5', 'marca': 'Chanel', 'genero': 'F', 'tamanho_ml': 100},
        {'nome': 'Chanel N°5', 'marca': 'Chanel', 'genero': 'F', 'tamanho_ml': 50},
        {'nome': 'Bleu de Chanel', 'marca': 'Chanel', 'genero': 'M', 'tamanho_ml': 100},
        {'nome': 'Sauvage', 'marca': 'Dior', 'genero': 'M', 'tamanho_ml': 100},
        {'nome': 'Sauvage', 'marca': 'Dior', 'genero': 'M', 'tamanho_ml': 60},
        {'nome': 'Miss Dior', 'marca': 'Dior', 'genero': 'F', 'tamanho_ml': 100},
        {'nome': 'Eros', 'marca': 'Versace', 'genero': 'M', 'tamanho_ml': 100},
        {'nome': 'Bright Crystal', 'marca': 'Versace', 'genero': 'F', 'tamanho_ml': 90},
        {'nome': 'Good Girl', 'marca': 'Carolina Herrera', 'genero': 'F', 'tamanho_ml': 80},
        {'nome': '212 VIP', 'marca': 'Carolina Herrera', 'genero': 'M', 'tamanho_ml': 100},
        {'nome': 'One Million', 'marca': 'Paco Rabanne', 'genero': 'M', 'tamanho_ml': 100},
        {'nome': 'Lady Million', 'marca': 'Paco Rabanne', 'genero': 'F', 'tamanho_ml': 80},
    ]
    
    perfumes = []
    for perfume_data in perfumes_data:
        perfume, created = Perfume.objects.get_or_create(
            nome=perfume_data['nome'],
            marca=marcas[perfume_data['marca']],
            genero=perfume_data['genero'],
            tamanho_ml=perfume_data['tamanho_ml'],
            defaults={'descricao': f"Perfume {perfume_data['nome']} {perfume_data['tamanho_ml']}ml"}
        )
        perfumes.append(perfume)
        print(f"  ✓ {perfume}")
    
    # Criar Clientes
    print("\n👥 Criando clientes...")
    clientes_data = [
        {'nome': 'Maria Silva', 'genero': 'F', 'celular': '(11) 98765-4321', 'instagram': '@mariasilva'},
        {'nome': 'João Santos', 'genero': 'M', 'celular': '(11) 97654-3210', 'instagram': '@joaosantos'},
        {'nome': 'Ana Costa', 'genero': 'F', 'celular': '(11) 96543-2109', 'instagram': '@anacosta'},
        {'nome': 'Pedro Oliveira', 'genero': 'M', 'celular': '(11) 95432-1098', 'instagram': '@pedrooliveira'},
        {'nome': 'Juliana Souza', 'genero': 'F', 'celular': '(11) 94321-0987', 'instagram': '@julianasouza'},
    ]
    
    clientes = []
    for cliente_data in clientes_data:
        cliente, created = Cliente.objects.get_or_create(
            celular=cliente_data['celular'],
            defaults=cliente_data
        )
        clientes.append(cliente)
        print(f"  ✓ {cliente.nome}")
    
    # Criar Vendas de Exemplo
    print("\n💰 Criando vendas de exemplo...")
    
    # Venda 1
    venda1 = Venda.objects.create(
        cliente=clientes[0],
        status='E',
        observacoes='Primeira compra da cliente'
    )
    ItemVenda.objects.create(
        venda=venda1,
        perfume=perfumes[0],  # Chanel N°5 100ml
        quantidade=1,
        preco_custo=Decimal('350.00'),
        preco_venda=Decimal('520.00')
    )
    venda1.valor_total = venda1.calcular_total()
    venda1.save()
    print(f"  ✓ Venda #{venda1.id} - {venda1.cliente.nome} - R$ {venda1.valor_total}")
    
    # Venda 2
    venda2 = Venda.objects.create(
        cliente=clientes[1],
        status='E'
    )
    ItemVenda.objects.create(
        venda=venda2,
        perfume=perfumes[3],  # Sauvage 100ml
        quantidade=1,
        preco_custo=Decimal('380.00'),
        preco_venda=Decimal('550.00')
    )
    ItemVenda.objects.create(
        venda=venda2,
        perfume=perfumes[2],  # Bleu de Chanel
        quantidade=1,
        preco_custo=Decimal('400.00'),
        preco_venda=Decimal('580.00')
    )
    venda2.valor_total = venda2.calcular_total()
    venda2.save()
    print(f"  ✓ Venda #{venda2.id} - {venda2.cliente.nome} - R$ {venda2.valor_total}")
    
    # Venda 3
    venda3 = Venda.objects.create(
        cliente=clientes[2],
        status='C'
    )
    ItemVenda.objects.create(
        venda=venda3,
        perfume=perfumes[8],  # Good Girl
        quantidade=2,
        preco_custo=Decimal('320.00'),
        preco_venda=Decimal('480.00')
    )
    venda3.valor_total = venda3.calcular_total()
    venda3.save()
    print(f"  ✓ Venda #{venda3.id} - {venda3.cliente.nome} - R$ {venda3.valor_total}")
    
    print("\n✅ Banco de dados populado com sucesso!")
    print(f"\n📊 Resumo:")
    print(f"  • {Marca.objects.count()} marcas")
    print(f"  • {Perfume.objects.count()} perfumes")
    print(f"  • {Cliente.objects.count()} clientes")
    print(f"  • {Venda.objects.count()} vendas")
    print(f"  • {ItemVenda.objects.count()} itens vendidos")
    print(f"\n🔐 Acesse o sistema:")
    print(f"  URL: http://127.0.0.1:8000")
    print(f"  Admin: http://127.0.0.1:8000/admin")
    print(f"  Usuário: admin")
    print(f"  Senha: admin (configure com: python3 manage.py changepassword admin)")

if __name__ == '__main__':
    popular()
