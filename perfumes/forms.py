from django import forms
from django.forms import inlineformset_factory
from .models import Marca, Perfume, Cliente, Venda, ItemVenda


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome', 'descricao', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm',
                'placeholder': 'Nome da marca'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm',
                'rows': 3, 'placeholder': 'Descrição da marca'
            }),
            'ativo': forms.CheckboxInput(attrs={'class': 'w-4 h-4 rounded'})
        }


class PerfumeForm(forms.ModelForm):
    class Meta:
        model = Perfume
        fields = ['nome', 'marca', 'genero', 'tamanho_ml', 'descricao', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm',
                'placeholder': 'Nome do perfume'
            }),
            'marca': forms.Select(attrs={'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm'}),
            'genero': forms.Select(attrs={'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm'}),
            'tamanho_ml': forms.Select(attrs={'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm'}),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm',
                'rows': 3, 'placeholder': 'Descrição do perfume'
            }),
            'ativo': forms.CheckboxInput(attrs={'class': 'w-4 h-4 rounded'})
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'genero', 'instagram', 'celular', 'email', 'observacoes', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm',
                'placeholder': 'Nome completo'
            }),
            'genero': forms.Select(attrs={'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm'}),
            'instagram': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm',
                'placeholder': '@usuario'
            }),
            'celular': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm',
                'placeholder': '(00) 00000-0000'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm',
                'placeholder': 'email@exemplo.com'
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm',
                'rows': 3, 'placeholder': 'Observações sobre o cliente'
            }),
            'ativo': forms.CheckboxInput(attrs={'class': 'w-4 h-4 rounded'})
        }


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'status', 'observacoes']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm'}),
            'status': forms.Select(attrs={'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm'}),
            'observacoes': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm',
                'rows': 3, 'placeholder': 'Observações sobre a venda'
            })
        }


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['perfume', 'quantidade', 'preco_custo', 'preco_venda']
        widgets = {
            'perfume': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-200 rounded-lg text-sm'}),
            'quantidade': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-200 rounded-lg text-sm', 'min': 1
            }),
            'preco_custo': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-200 rounded-lg text-sm',
                'step': '0.01', 'min': '0', 'placeholder': '0.00'
            }),
            'preco_venda': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-200 rounded-lg text-sm',
                'step': '0.01', 'min': '0', 'placeholder': '0.00'
            })
        }


ItemVendaFormSet = inlineformset_factory(
    Venda,
    ItemVenda,
    form=ItemVendaForm,
    extra=3,
    can_delete=True
)
