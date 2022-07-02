from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from .models import Fabricante, Genero, Perfume, Tamanho, Tipo, Cliente, Venda
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def logoff(request):
    return HttpResponseRedirect('login')

def sair(request):
    logout(request)
    return HttpResponseRedirect('login')

def cadastrar_usuario(request):  
    if request.user.is_authenticated:
        if request.method == "POST":
            form_usuario = UserCreationForm(request.POST)
            if form_usuario.is_valid():
                form_usuario.save()
                return HttpResponseRedirect('login')
        else:
            form_usuario = UserCreationForm()
        return render(request, 'cadastro.html', {'form_usuario': form_usuario})
    else:
        return HttpResponseRedirect('login')
    
    

def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username,password)

        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            print("autenticou")
            return redirect('menu')
        else:
            print("nao autenticou")
            return HttpResponseRedirect('login')
    else:
        return render(request, 'index.html')

# Menu
def menu(request):
    if request.user.is_authenticated:
        return render(request,'menu.html')
    else:
        return render(request,'logoff.html')

# Tamanhos
def listagemtamanhos(request):
    if request.user.is_authenticated:
        tamanhos = Tamanho.objects.all().order_by('nome')
        if request.method == 'POST':
            if request.POST.get('nome'):
                post = Tamanho()
                post.nome = request.POST.get('nome')
                post.save()
            return render(request, 'listagemtamanhos.html',context={'tamanhos':tamanhos})
        else:
            return render(request, 'listagemtamanhos.html',context={'tamanhos':tamanhos})
    else:
        return render(request,'logoff.html')

def deletar_tamanho(request,id):
    if request.user.is_authenticated:
        try:
            registro = Tamanho.objects.get(id =id)
            registro.delete()
            tamanhos = Tamanho.objects.all().order_by('nome')
            return redirect(request.META['HTTP_REFERER'])
        except:
            messages.info(request, 'Não é possível excluir o tamanho selecionado pois ele está sendo utilizado em algum perfume cadastrado')
            tamanhos = Tamanho.objects.all().order_by('nome')
            return render(request,'listagemtamanhos.html',{'tamanhos':tamanhos})
    else:
        return render(request,'logoff.html')
    
# Perfumes

def listagemperfumes(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('nome'):
                id_tipo = int(request.POST.get('tipo'))
                id_fabricante = int(request.POST.get('fabricante'))
                id_genero = int(request.POST.get('genero'))
                id_tamanho = int(request.POST.get('tamanho'))
                post = Perfume(nome=request.POST.get('nome'),fabricante_id=id_fabricante,genero_id=id_genero,tamanho_id=id_tamanho,tipo_id=id_tipo)
                post.save()
                perfumes = Perfume.objects.all().order_by('nome')
                fabricantes = Fabricante.objects.all().order_by('nome')
                generos = Genero.objects.all().order_by('nome')
                tamanhos = Tamanho.objects.all().order_by('nome')
                return render(request, 'listagemperfumes.html',context={'perfumes':perfumes,'fabricantes':fabricantes,'generos':generos,'tamanhos':tamanhos})
        else:
            perfumes = Perfume.objects.all().order_by('nome')
            fabricantes = Fabricante.objects.all().order_by('nome')
            generos = Genero.objects.all().order_by('nome')
            tamanhos = Tamanho.objects.all().order_by('nome')
            tipos = Tipo.objects.all().order_by('nome')
        return render(request, 'listagemperfumes.html',context={'perfumes':perfumes,'fabricantes':fabricantes,'generos':generos,'tamanhos':tamanhos,'tipos':tipos})
    else:
        return render(request,'logoff.html')

def deletar_perfume(request,id):
    if request.user.is_authenticated:
        try:
            registro = Perfume.objects.get(id =id)
            registro.delete()
            perfumes = Perfume.objects.all().order_by('nome')
            return render(request,'listagemperfumes.html',{'perfumes':perfumes})
        except:
            messages.info(request, 'Não é possível excluir o perfume selecionado pois ele está sendo utilizado em alguma venda cadastrada')
            perfumes = Perfume.objects.all().order_by('nome')
        return render(request,'listagemperfumes.html',{'perfumes':perfumes})
    else:
        return render(request,'logoff.html')

# Fabricantes
def listagemfabricantes(request):
    if request.user.is_authenticated:
        fabricantes = Fabricante.objects.all().order_by('nome')
        if request.method == 'POST':
            if request.POST.get('nome'):
                post = Fabricante()
                post.nome = request.POST.get('nome')
                post.save()
            return render(request, 'listagemfabricantes.html',context={'fabricantes':fabricantes})
        else:
            return render(request, 'listagemfabricantes.html',context={'fabricantes':fabricantes})
    else:
        return render(request,'logoff.html')

def deletar_fabricante(request,id):
    if request.user.is_authenticated:
        try:
            registro = Fabricante.objects.get(id =id)
            registro.delete()
            fabricantes = Fabricante.objects.all().order_by('nome')
            return redirect(request.META['HTTP_REFERER'])
        except:
            messages.info(request, 'Não é possível excluir o fabricante selecionado pois ele está sendo utilizado em algum perfume cadastrado')
            fabricantes = Fabricante.objects.all().order_by('nome')
            return render(request,'listagemfabricantes.html',{'fabricantes':fabricantes})
    else:
        return render(request,'logoff.html')
# Tipos
def listagemtipos(request):
    if request.user.is_authenticated:
        tipos = Tipo.objects.all().order_by('nome')
        if request.method == 'POST':
            if request.POST.get('nome'):
                post = Tipo()
                post.nome = request.POST.get('nome')
                post.save()
            return render(request, 'listagemtipos.html',context={'tipos':tipos})
        else:
            return render(request, 'listagemtipos.html',context={'tipos':tipos})
    else:
        return render(request,'logoff.html')

def deletar_tipo(request,id):
    if request.user.is_authenticated:
        try:
            registro = Tipo.objects.get(id =id)
            registro.delete()
            tipos = Tipo.objects.all().order_by('nome')
            return redirect(request.META['HTTP_REFERER'])
        except:
            messages.info(request, 'Não é possível excluir o tipo selecionado pois ele está sendo utilizado em algum perfume cadastrado')
            tipos = Tipo.objects.all().order_by('nome')
            return render(request,'listagemtipos.html',{'tipos':tipos})
    else:
        return render(request,'logoff.html')  
# Clientes

def listagemclientes(request):
    if request.user.is_authenticated:
        clientes = Cliente.objects.all().order_by('nome')
        if request.method == 'POST':
            if request.POST.get('nome'):
                post = Cliente()
                post.nome = request.POST.get('nome')
                post.telefone = request.POST.get('telefone')
                post.save()
            return render(request, 'listagemclientes.html',context={'clientes':clientes})
        else:
            return render(request, 'listagemclientes.html',context={'clientes':clientes})
    else:
        return render(request,'logoff.html')

def deletar_cliente(request,id):
    if request.user.is_authenticated:
        try:
            registro = Cliente.objects.get(id =id)
            registro.delete()
            clientes = Cliente.objects.all().order_by('nome')
            return redirect(request.META['HTTP_REFERER'])
        except:
            messages.info(request, 'Não é possível excluir o cliente selecionado pois ele está sendo utilizado em alguma venda cadastrada')
            clientes = Cliente.objects.all().order_by('nome')
            return render(request,'listagemclientes.html',{'clientes':clientes})
    else:
        return render(request,'logoff.html')

# Vendas

def listagemvendas(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id_perfume = int(request.POST.get('perfume'))
            id_cliente = int(request.POST.get('cliente'))
            preco_de_custo = request.POST.get('preco_de_custo')
            preco_de_venda = request.POST.get('preco_de_venda')
            post = Venda(perfume_id=id_perfume,cliente_id=id_cliente,preco_custo=preco_de_custo,preco_venda=preco_de_venda)
            post.save()
            perfumes = Perfume.objects.all().order_by('nome')
            clientes = Cliente.objects.all().order_by('nome')
            vendas = Venda.objects.all()
            return redirect(request.META['HTTP_REFERER'])
            #return render(request, 'listagemvendas.html',context={'vendas':vendas,'perfumes':perfumes,'clientes':clientes})
        else:
            perfumes = Perfume.objects.all().order_by('nome')
            clientes = Cliente.objects.all().order_by('nome')
            vendas = Venda.objects.all()
        return render(request, 'listagemvendas.html',context={'vendas':vendas,'perfumes':perfumes,'clientes':clientes})
    else:
        return render(request,'logoff.html')

def deletar_venda(request,id):
    if request.user.is_authenticated:
        try:
            registro = Venda.objects.get(id =id)
            registro.delete()
            vendas = Venda.objects.all()
            return redirect(request.META['HTTP_REFERER'])
        except:
            messages.info(request, 'Não é possível excluir a venda selecionada')
            vendas = Venda.objects.all()
        return render(request,'listagemvendas.html',{'vendas':vendas})
    else:
        return render(request,'logoff.html')

def dashboard(request):
    if request.user.is_authenticated:
        qt_jan = Venda.objects.filter(data_venda__year='2022', data_venda__month='1').count()
        qt_fev = Venda.objects.filter(data_venda__year='2022', data_venda__month='2').count()
        qt_mar = Venda.objects.filter(data_venda__year='2022', data_venda__month='3').count()
        qt_abr = Venda.objects.filter(data_venda__year='2022', data_venda__month='4').count()
        qt_mai = Venda.objects.filter(data_venda__year='2022', data_venda__month='5').count()
        qt_jun = Venda.objects.filter(data_venda__year='2022', data_venda__month='6').count()
        qt_jul = Venda.objects.filter(data_venda__year='2022', data_venda__month='7').count()
        qt_ago = Venda.objects.filter(data_venda__year='2022', data_venda__month='8').count()
        qt_set = Venda.objects.filter(data_venda__year='2022', data_venda__month='9').count()
        qt_out = Venda.objects.filter(data_venda__year='2022', data_venda__month='10').count()
        qt_nov = Venda.objects.filter(data_venda__year='2022', data_venda__month='11').count()
        qt_dez = Venda.objects.filter(data_venda__year='2022', data_venda__month='12').count()
        
        #list_result = [resultado for resultado in resultados]  # converts ValuesQuerySet into Python list
        meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        valores = [qt_jan,qt_fev,qt_mar,qt_abr,qt_mai,qt_jun,qt_jul,qt_ago,qt_set,qt_out,qt_nov,qt_dez]
        plt.bar(meses,valores)
        plt.xticks(rotation=12)
        fig = plt.gcf()
        fig.set_size_inches(11,5)
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        return render(request,'dashboard.html',{'data':uri})
    else:
        return render(request,'logoff.html')
