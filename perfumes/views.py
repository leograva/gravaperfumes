from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import date, timedelta
from decimal import Decimal
from .models import Marca, Perfume, Cliente, Venda, ItemVenda
from .forms import MarcaForm, PerfumeForm, ClienteForm, VendaForm, ItemVendaFormSet


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'perfumes/login.html', {'error': 'Usuário ou senha incorretos'})
    return render(request, 'perfumes/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    hoje = timezone.now().date()

    # --- Período selecionado ---
    periodo = request.GET.get('periodo', 'mes')
    data_inicio_str = request.GET.get('data_inicio', '')
    data_fim_str = request.GET.get('data_fim', '')

    if periodo == 'hoje':
        data_inicio = hoje
        data_fim = hoje
    elif periodo == 'semana':
        data_inicio = hoje - timedelta(days=6)
        data_fim = hoje
    elif periodo == 'mes':
        data_inicio = hoje.replace(day=1)
        data_fim = hoje
    elif periodo == 'trimestre':
        data_inicio = (hoje - timedelta(days=89)).replace(day=1)
        data_fim = hoje
    elif periodo == 'ano':
        data_inicio = hoje.replace(month=1, day=1)
        data_fim = hoje
    elif periodo == 'personalizado' and data_inicio_str and data_fim_str:
        try:
            data_inicio = date.fromisoformat(data_inicio_str)
            data_fim = date.fromisoformat(data_fim_str)
        except ValueError:
            data_inicio = hoje.replace(day=1)
            data_fim = hoje
    else:
        data_inicio = hoje.replace(day=1)
        data_fim = hoje

    # --- Queryset filtrado pelo período ---
    vendas_periodo = Venda.objects.filter(
        data_venda__date__gte=data_inicio,
        data_venda__date__lte=data_fim,
    )

    total_vendas = vendas_periodo.filter(status__in=['C', 'E']).aggregate(
        total=Sum('valor_total')
    )['total'] or Decimal('0.00')

    total_lucro = Decimal('0.00')
    for v in vendas_periodo.filter(status__in=['C', 'E']).prefetch_related('itens'):
        total_lucro += v.calcular_lucro()

    qtd_vendas_periodo = vendas_periodo.count()
    ticket_medio = (total_vendas / qtd_vendas_periodo) if qtd_vendas_periodo else Decimal('0.00')

    # --- Totais gerais (não filtrados por período) ---
    total_clientes = Cliente.objects.filter(ativo=True).count()
    total_perfumes = Perfume.objects.filter(ativo=True).count()

    # --- Vendas recentes do período ---
    vendas_recentes = vendas_periodo.select_related('cliente').order_by('-data_venda')[:8]

    # --- Dados para o gráfico (agrupado por mês, só confirmadas/entregues) ---
    from django.db.models.functions import TruncMonth
    import json

    vendas_confirmadas = vendas_periodo.filter(status__in=['C', 'E'])

    vendas_por_mes = (
        vendas_confirmadas
        .annotate(mes=TruncMonth('data_venda'))
        .values('mes')
        .annotate(total=Sum('valor_total'))
        .order_by('mes')
    )

    lucro_por_mes_dict = {}
    for v in vendas_confirmadas.prefetch_related('itens'):
        mes_key = v.data_venda.strftime('%Y-%m')
        lucro_por_mes_dict[mes_key] = lucro_por_mes_dict.get(mes_key, Decimal('0')) + v.calcular_lucro()

    MESES_PT = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
    labels_grafico, dados_vendas, dados_lucro = [], [], []

    for item in vendas_por_mes:
        mes_dt  = item['mes']
        mes_key = mes_dt.strftime('%Y-%m')
        labels_grafico.append(f"{MESES_PT[mes_dt.month - 1]}/{mes_dt.strftime('%y')}")
        dados_vendas.append(float(item['total'] or 0))
        dados_lucro.append(float(lucro_por_mes_dict.get(mes_key, 0)))

    context = {
        'total_vendas': total_vendas,
        'total_lucro': total_lucro,
        'ticket_medio': ticket_medio,
        'qtd_vendas_periodo': qtd_vendas_periodo,
        'total_clientes': total_clientes,
        'total_perfumes': total_perfumes,
        'vendas_recentes': vendas_recentes,
        'periodo': periodo,
        'data_inicio': data_inicio.isoformat(),
        'data_fim': data_fim.isoformat(),
        'data_inicio_fmt': data_inicio.strftime('%d/%m/%Y'),
        'data_fim_fmt': data_fim.strftime('%d/%m/%Y'),
        'periodo_opcoes': [
            ('hoje',      'Hoje'),
            ('semana',    'Últimos 7 dias'),
            ('mes',       'Este mês'),
            ('trimestre', 'Trimestre'),
            ('ano',       'Este ano'),
        ],
        'labels_grafico': json.dumps(labels_grafico),
        'dados_vendas':   json.dumps(dados_vendas),
        'dados_lucro':    json.dumps(dados_lucro),
    }
    return render(request, 'perfumes/dashboard.html', context)


# Views de Marcas
@login_required(login_url='login')
def marca_lista(request):
    marcas = Marca.objects.annotate(
        qtd_perfumes=Count('perfumes')
    ).order_by('nome')
    return render(request, 'perfumes/marca_lista.html', {'marcas': marcas})


@login_required(login_url='login')
def marca_criar(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca criada com sucesso!')
            return redirect('marca_lista')
    else:
        form = MarcaForm()
    return render(request, 'perfumes/marca_form.html', {'form': form, 'titulo': 'Nova Marca'})


@login_required(login_url='login')
def marca_editar(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca atualizada com sucesso!')
            return redirect('marca_lista')
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'perfumes/marca_form.html', {'form': form, 'titulo': 'Editar Marca'})


# Views de Perfumes
@login_required(login_url='login')
def perfume_lista(request):
    perfumes = Perfume.objects.select_related('marca').filter(ativo=True)
    
    # Filtros
    marca_id = request.GET.get('marca')
    genero = request.GET.get('genero')
    tamanho = request.GET.get('tamanho')
    busca = request.GET.get('busca')
    
    if marca_id:
        perfumes = perfumes.filter(marca_id=marca_id)
    if genero:
        perfumes = perfumes.filter(genero=genero)
    if tamanho:
        perfumes = perfumes.filter(tamanho_ml=tamanho)
    if busca:
        perfumes = perfumes.filter(
            Q(nome__icontains=busca) | Q(marca__nome__icontains=busca)
        )
    
    marcas = Marca.objects.filter(ativo=True)
    
    context = {
        'perfumes': perfumes,
        'marcas': marcas,
        'generos': Perfume.GENERO_CHOICES,
        'tamanhos': Perfume.TAMANHO_CHOICES,
    }
    return render(request, 'perfumes/perfume_lista.html', context)


@login_required(login_url='login')
def perfume_criar(request):
    if request.method == 'POST':
        form = PerfumeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfume criado com sucesso!')
            return redirect('perfume_lista')
    else:
        form = PerfumeForm()
    return render(request, 'perfumes/perfume_form.html', {'form': form, 'titulo': 'Novo Perfume'})


@login_required(login_url='login')
def perfume_editar(request, pk):
    perfume = get_object_or_404(Perfume, pk=pk)
    if request.method == 'POST':
        form = PerfumeForm(request.POST, instance=perfume)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfume atualizado com sucesso!')
            return redirect('perfume_lista')
    else:
        form = PerfumeForm(instance=perfume)
    return render(request, 'perfumes/perfume_form.html', {'form': form, 'titulo': 'Editar Perfume'})


# Views de Clientes
@login_required(login_url='login')
def cliente_lista(request):
    clientes = Cliente.objects.filter(ativo=True).annotate(
        qtd_compras=Count('vendas'),
        total_gasto=Sum('vendas__valor_total')
    )
    
    busca = request.GET.get('busca')
    if busca:
        clientes = clientes.filter(
            Q(nome__icontains=busca) | 
            Q(celular__icontains=busca) | 
            Q(instagram__icontains=busca)
        )
    
    return render(request, 'perfumes/cliente_lista.html', {'clientes': clientes})


@login_required(login_url='login')
def cliente_criar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente criado com sucesso!')
            return redirect('cliente_lista')
    else:
        form = ClienteForm()
    return render(request, 'perfumes/cliente_form.html', {'form': form, 'titulo': 'Novo Cliente'})


@login_required(login_url='login')
def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('cliente_lista')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'perfumes/cliente_form.html', {'form': form, 'titulo': 'Editar Cliente'})


@login_required(login_url='login')
def cliente_detalhe(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    vendas = cliente.vendas.all()[:10]
    return render(request, 'perfumes/cliente_detalhe.html', {'cliente': cliente, 'vendas': vendas})


# Views de Vendas
@login_required(login_url='login')
def venda_lista(request):
    vendas = Venda.objects.select_related('cliente').prefetch_related('itens')
    
    status = request.GET.get('status')
    if status:
        vendas = vendas.filter(status=status)
    
    return render(request, 'perfumes/venda_lista.html', {
        'vendas': vendas,
        'status_choices': Venda.STATUS_CHOICES
    })


@login_required(login_url='login')
def venda_criar(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        formset = ItemVendaFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            venda = form.save()
            
            for item_form in formset:
                if item_form.cleaned_data and not item_form.cleaned_data.get('DELETE'):
                    item = item_form.save(commit=False)
                    item.venda = venda
                    item.save()
            
            venda.valor_total = venda.calcular_total()
            venda.save()
            
            messages.success(request, 'Venda criada com sucesso!')
            return redirect('venda_detalhe', pk=venda.pk)
    else:
        form = VendaForm()
        formset = ItemVendaFormSet()
    
    return render(request, 'perfumes/venda_form.html', {
        'form': form,
        'formset': formset,
        'titulo': 'Nova Venda'
    })


@login_required(login_url='login')
def venda_detalhe(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    itens = venda.itens.select_related('perfume__marca')
    
    context = {
        'venda': venda,
        'itens': itens,
        'lucro_total': venda.calcular_lucro()
    }
    return render(request, 'perfumes/venda_detalhe.html', context)


@login_required(login_url='login')
def venda_editar_status(request, pk):
    if request.method == 'POST':
        venda = get_object_or_404(Venda, pk=pk)
        novo_status = request.POST.get('status')
        if novo_status in dict(Venda.STATUS_CHOICES):
            venda.status = novo_status
            venda.save()
            messages.success(request, 'Status atualizado com sucesso!')
        return redirect('venda_detalhe', pk=pk)


@login_required(login_url='login')
def venda_deletar(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        numero = venda.id
        venda.delete()
        messages.success(request, f'Venda #{numero} excluída com sucesso.')
        return redirect('venda_lista')
    return redirect('venda_detalhe', pk=pk)
