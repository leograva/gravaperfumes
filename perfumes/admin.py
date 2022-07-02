from django.contrib import admin
from .models import Cliente,Perfume,Fabricante,Genero,Tamanho,Venda

# Register your models here.
admin.site.register(Perfume)
admin.site.register(Fabricante)
admin.site.register(Genero)
admin.site.register(Tamanho)
admin.site.register(Cliente)
admin.site.register(Venda)