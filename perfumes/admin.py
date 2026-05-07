from django.contrib import admin
from django.db.models import Sum, Count, F
from django.utils.html import format_html
from .models import Marca, Perfume, Cliente, Venda, ItemVenda


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'quantidade_perfumes', 'ativo', 'criado_em']
    list_filter = ['ativo', 'criado_em']
    search_fields = ['nome', 'descricao']
    ordering = ['nome']
    
    def quantidade_perfumes(self, obj):
        return obj.perfumes.count()
    quantidade_perfumes.short_description = 'Qtd. Perfumes'


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'marca', 'genero', 'tamanho_ml', 'ativo']
    list_filter = ['marca', 'genero', 'tamanho_ml', 'ativo']
    search_fields = ['nome', 'marca__nome', 'descricao']
    ordering = ['marca', 'nome', 'tamanho_ml']
    list_per_page = 50
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'marca', 'genero', 'tamanho_ml')
        }),
        ('Detalhes', {
            'fields': ('descricao', 'ativo')
        }),
    )


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'genero', 'celular', 'instagram', 'quantidade_compras', 'total_compras', 'ativo']
    list_filter = ['genero', 'ativo', 'criado_em']
    search_fields = ['nome', 'celular', 'instagram', 'email']
    ordering = ['nome']
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'genero')
        }),
        ('Contato', {
            'fields': ('celular', 'instagram', 'email')
        }),
        ('Observações', {
            'fields': ('observacoes', 'ativo'),
            'classes': ('collapse',)
        }),
    )
    
    def quantidade_compras(self, obj):
        return obj.quantidade_compras()
    quantidade_compras.short_description = 'Qtd. Compras'
    
    def total_compras(self, obj):
        total = obj.total_compras()
        return format_html('<strong>R$ {:.2f}</strong>', total)
    total_compras.short_description = 'Total Comprado'


class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1
    fields = ['perfume', 'quantidade', 'preco_custo', 'preco_venda', 'subtotal_display', 'lucro_display']
    readonly_fields = ['subtotal_display', 'lucro_display']
    
    def subtotal_display(self, obj):
        if obj.id:
            return format_html('<strong>R$ {:.2f}</strong>', obj.subtotal())
        return '-'
    subtotal_display.short_description = 'Subtotal'
    
    def lucro_display(self, obj):
        if obj.id:
            lucro = obj.lucro()
            cor = 'green' if lucro > 0 else 'red'
            return format_html('<strong style="color: {};">R$ {:.2f}</strong>', cor, lucro)
        return '-'
    lucro_display.short_description = 'Lucro'


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'data_venda', 'status', 'valor_total_display', 'lucro_display', 'quantidade_itens']
    list_filter = ['status', 'data_venda']
    search_fields = ['cliente__nome', 'observacoes']
    ordering = ['-data_venda']
    date_hierarchy = 'data_venda'
    inlines = [ItemVendaInline]
    
    fieldsets = (
        ('Informações da Venda', {
            'fields': ('cliente', 'status')
        }),
        ('Observações', {
            'fields': ('observacoes',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['valor_total']
    
    def valor_total_display(self, obj):
        return format_html('<strong>R$ {:.2f}</strong>', obj.valor_total)
    valor_total_display.short_description = 'Valor Total'
    valor_total_display.admin_order_field = 'valor_total'
    
    def lucro_display(self, obj):
        lucro = obj.calcular_lucro()
        cor = 'green' if lucro > 0 else 'red'
        return format_html('<strong style="color: {};">R$ {:.2f}</strong>', cor, lucro)
    lucro_display.short_description = 'Lucro'
    
    def quantidade_itens(self, obj):
        return obj.itens.count()
    quantidade_itens.short_description = 'Qtd. Itens'
    
    def save_model(self, request, obj, form, change):
        """Salva o modelo e atualiza o valor total"""
        super().save_model(request, obj, form, change)
        obj.valor_total = obj.calcular_total()
        obj.save(update_fields=['valor_total'])


@admin.register(ItemVenda)
class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ['venda', 'perfume', 'quantidade', 'preco_custo', 'preco_venda', 'subtotal_display', 'lucro_display', 'margem_display']
    list_filter = ['venda__data_venda', 'perfume__marca', 'perfume__genero']
    search_fields = ['venda__cliente__nome', 'perfume__nome']
    ordering = ['-venda__data_venda']
    
    def subtotal_display(self, obj):
        return format_html('R$ {:.2f}', obj.subtotal())
    subtotal_display.short_description = 'Subtotal'
    
    def lucro_display(self, obj):
        lucro = obj.lucro()
        cor = 'green' if lucro > 0 else 'red'
        return format_html('<strong style="color: {};">R$ {:.2f}</strong>', cor, lucro)
    lucro_display.short_description = 'Lucro'
    
    def margem_display(self, obj):
        margem = obj.margem_lucro_percentual()
        cor = 'green' if margem > 0 else 'red'
        return format_html('<strong style="color: {};">{:.1f}%</strong>', cor, margem)
    margem_display.short_description = 'Margem %'
