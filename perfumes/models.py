from django.db import models
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.
class Fabricante(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tamanho(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Perfume(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT) 
    tamanho = models.ForeignKey(Tamanho, on_delete=models.PROTECT) 
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.nome

class Venda(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.PROTECT) 
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT) 
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateField(auto_now=True)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, ' ')))
        return ' - '.join(field_values)