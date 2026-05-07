from django import forms
from django.forms import inlineformset_factory
from .models import Marca, Perfume, Cliente, Venda, ItemVenda


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome', 'descricao', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral',
                'placeholder': 'Nome da marca'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral',
                'rows': 3,
                'placeholder': 'Descrição da marca'
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-grava-coral focus:ring-grava-coral border-grava-beige rounded'
            })
        }


class PerfumeForm(forms.ModelForm):
    class Meta:
        model = Perfume
        fields = ['nome', 'marca', 'genero', 'tamanho_ml', 'descricao', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral',
                'placeholder': 'Nome do perfume'
            }),
            'marca': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral'
            }),
            'genero': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral'
            }),
            'tamanho_ml': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral',
                'rows': 3,
                'placeholder': 'Descrição do perfume'
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-grava-coral focus:ring-grava-coral border-grava-beige rounded'
            })
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'genero', 'instagram', 'celular', 'email', 'observacoes', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral',
                'placeholder': 'Nome completo'
            }),
            'genero': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral'
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral',
                'placeholder': '@usuario'
            }),
            'celular': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral',
                'placeholder': '(00) 00000-0000'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral',
                'placeholder': 'email@exemplo.com'
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral',
                'rows': 3,
                'placeholder': 'Observações sobre o cliente'
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-grava-coral focus:ring-grava-coral border-grava-beige rounded'
            })
        }


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'status', 'observacoes']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral'
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral',
                'rows': 3,
                'placeholder': 'Observações sobre a venda'
            })
        }


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['perfume', 'quantidade', 'preco_custo', 'preco_venda']
        widgets = {
            'perfume': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral text-sm'
            }),
            'quantidade': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral text-sm',
                'min': 1
            }),
            'preco_custo': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral text-sm',
                'step': '0.01',
                'min': '0'
            }),
            'preco_venda': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border-2 border-grava-beige rounded-lg focus:ring-2 focus:ring-grava-coral focus:border-grava-coral text-sm',
                'step': '0.01',
                'min': '0'
            })
        }


ItemVendaFormSet = inlineformset_factory(
    Venda,
    ItemVenda,
    form=ItemVendaForm,
    extra=3,
    can_delete=True
)
