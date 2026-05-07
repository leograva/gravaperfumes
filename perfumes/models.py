from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Marca(models.Model):
    """Marca dos perfumes"""
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Perfume(models.Model):
    """Catálogo de perfumes"""
    GENERO_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('U', 'Unissex'),
    ]
    
    TAMANHO_CHOICES = [
        (25, '25ml'),
        (30, '30ml'),
        (50, '50ml'),
        (75, '75ml'),
        (80, '80ml'),
        (90, '90ml'),
        (100, '100ml'),
        (150, '150ml'),
        (200, '200ml'),
    ]
    
    nome = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='perfumes')
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    tamanho_ml = models.IntegerField(choices=TAMANHO_CHOICES)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Perfume'
        verbose_name_plural = 'Perfumes'
        ordering = ['marca', 'nome', 'tamanho_ml']
        unique_together = ['nome', 'marca', 'genero', 'tamanho_ml']
    
    def __str__(self):
        return f"{self.marca.nome} - {self.nome} ({self.get_genero_display()}) - {self.tamanho_ml}ml"


class Cliente(models.Model):
    """Cadastro de clientes"""
    GENERO_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outro'),
        ('N', 'Prefiro não informar'),
    ]
    
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True)
    instagram = models.CharField(max_length=100, blank=True, help_text='@usuario')
    celular = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    observacoes = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    def total_compras(self):
        """Retorna o valor total de compras do cliente"""
        return self.vendas.aggregate(
            total=models.Sum('valor_total')
        )['total'] or Decimal('0.00')
    
    def quantidade_compras(self):
        """Retorna a quantidade de compras do cliente"""
        return self.vendas.count()


class Venda(models.Model):
    """Registro de vendas"""
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('C', 'Confirmada'),
        ('E', 'Entregue'),
        ('X', 'Cancelada'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='vendas')
    data_venda = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    observacoes = models.TextField(blank=True)
    valor_total = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering = ['-data_venda']
    
    def __str__(self):
        return f"Venda #{self.id} - {self.cliente.nome} - {self.data_venda.strftime('%d/%m/%Y')}"
    
    def calcular_total(self):
        """Calcula o valor total da venda baseado nos itens"""
        total = self.itens.aggregate(
            total=models.Sum(
                models.F('preco_venda') * models.F('quantidade'),
                output_field=models.DecimalField()
            )
        )['total'] or Decimal('0.00')
        return total
    
    def calcular_lucro(self):
        """Calcula o lucro total da venda"""
        lucro = self.itens.aggregate(
            lucro=models.Sum(
                (models.F('preco_venda') - models.F('preco_custo')) * models.F('quantidade'),
                output_field=models.DecimalField()
            )
        )['lucro'] or Decimal('0.00')
        return lucro
    
    def save(self, *args, **kwargs):
        """Atualiza o valor total ao salvar"""
        super().save(*args, **kwargs)
        self.valor_total = self.calcular_total()
        if self.valor_total != self.valor_total:  # Evita loop infinito
            super().save(update_fields=['valor_total'])


class ItemVenda(models.Model):
    """Itens de cada venda"""
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    perfume = models.ForeignKey(Perfume, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    preco_custo = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        help_text='Preço de custo na data da venda'
    )
    preco_venda = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        help_text='Preço de venda para o cliente'
    )
    
    class Meta:
        verbose_name = 'Item da Venda'
        verbose_name_plural = 'Itens da Venda'
    
    def __str__(self):
        return f"{self.perfume.nome} - Qtd: {self.quantidade}"
    
    def subtotal(self):
        """Retorna o subtotal do item"""
        return self.preco_venda * self.quantidade
    
    def lucro(self):
        """Retorna o lucro do item"""
        return (self.preco_venda - self.preco_custo) * self.quantidade
    
    def margem_lucro_percentual(self):
        """Retorna a margem de lucro em percentual"""
        if self.preco_custo > 0:
            return ((self.preco_venda - self.preco_custo) / self.preco_custo) * 100
        return 0
    
    def save(self, *args, **kwargs):
        """Atualiza o total da venda ao salvar o item"""
        super().save(*args, **kwargs)
        self.venda.save()  # Atualiza o valor total da venda
