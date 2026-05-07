# 💐 Grava Perfumes - Sistema de Gestão de Vendas

Sistema moderno em Django para gestão de vendas de perfumes importados com interface elegante e funcional.

## 🎨 Características

- **Design Moderno**: Interface clean com as cores da marca (Roxo, Bege e Coral)
- **Autenticação**: Sistema de login seguro
- **Dashboard**: Visão geral com estatísticas em tempo real
- **Gestão Completa**: Clientes, Perfumes, Marcas e Vendas
- **Cálculo de Lucro**: Automático por venda e por item
- **Preços Flexíveis**: Defina custo e venda por transação
- **Responsivo**: Funciona em desktop, tablet e mobile

## 🚀 Deploy no Easypanel (Hostinger VPS)

### 1. Preparar o Repositório

```bash
# Inicializar git (se ainda não tiver)
git init
git add .
git commit -m "Initial commit"

# Criar repositório no GitHub/GitLab
git remote add origin seu-repositorio.git
git push -u origin main
```

### 2. Configurar no Easypanel

1. Acesse seu Easypanel na Hostinger
2. Clique em **"Create Service"** → **"App"**
3. Selecione **"GitHub"** ou **"GitLab"**
4. Escolha seu repositório
5. Configure:
   - **Name**: gravaperfumes
   - **Build Type**: Dockerfile
   - **Port**: 8000

### 3. Configurar Variáveis de Ambiente

No Easypanel, adicione as seguintes variáveis:

```env
SECRET_KEY=gere-uma-chave-secreta-forte-aqui
DEBUG=False
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
DB_ENGINE=django.db.backends.postgresql
DB_NAME=gravaperfumes
DB_USER=postgres
DB_PASSWORD=sua-senha-segura
DB_HOST=postgres
DB_PORT=5432
```

### 4. Adicionar Banco de Dados PostgreSQL

1. No Easypanel, clique em **"Create Service"** → **"Database"**
2. Selecione **"PostgreSQL"**
3. Configure:
   - **Name**: gravaperfumes-db
   - **Database**: gravaperfumes
   - **User**: postgres
   - **Password**: (use a mesma senha das variáveis)

### 5. Conectar App ao Banco

1. Vá nas configurações do seu app
2. Em **"Links"**, conecte ao banco PostgreSQL
3. O Easypanel criará automaticamente as variáveis de conexão

### 6. Deploy

1. Clique em **"Deploy"**
2. Aguarde o build e deploy
3. Após o deploy, execute os comandos:

```bash
# No terminal do Easypanel
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

### 7. Configurar Domínio

1. No Easypanel, vá em **"Domains"**
2. Adicione seu domínio
3. O Easypanel configurará SSL automaticamente

## 🔐 Primeiro Acesso

1. Acesse: `https://seu-dominio.com`
2. Faça login com o superusuário criado
3. Comece cadastrando marcas e perfumes!

## 📦 Estrutura do Projeto

```
gravaperfumes/
├── perfumes/              # App principal
│   ├── models.py         # Modelos de dados
│   ├── views.py          # Lógica das views
│   ├── forms.py          # Formulários
│   ├── urls.py           # Rotas
│   ├── templates/        # Templates HTML
│   └── static/           # Arquivos estáticos
├── gravaperfumes/        # Configurações
│   ├── settings.py       # Settings do Django
│   └── urls.py           # URLs principais
├── Dockerfile            # Configuração Docker
├── requirements.txt      # Dependências Python
├── .env.example         # Exemplo de variáveis
└── manage.py            # Gerenciador Django
```

## 🛠️ Desenvolvimento Local

```bash
# Instalar dependências
pip install -r requirements.txt

# Criar arquivo .env
cp .env.example .env

# Editar .env com suas configurações
# Para desenvolvimento, pode usar SQLite

# Migrar banco
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Popular dados de exemplo (opcional)
python popular_dados.py

# Iniciar servidor
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

## 🎯 Funcionalidades

### Dashboard
- Total de vendas
- Clientes ativos
- Perfumes cadastrados
- Vendas do mês
- Vendas recentes

### Gestão de Clientes
- Cadastro completo
- Histórico de compras
- Total gasto
- Busca e filtros

### Catálogo de Perfumes
- Organização por marca
- Filtros por gênero e tamanho
- Variações de 25ml a 200ml

### Vendas
- Múltiplos itens por venda
- Preço de custo e venda por item
- Cálculo automático de lucro
- Status da venda
- Margem de lucro percentual

## 🔒 Segurança

- Autenticação obrigatória
- CSRF protection
- SQL injection protection
- XSS protection
- SSL/HTTPS em produção

## 📱 Suporte

Para dúvidas ou problemas:
- Verifique os logs no Easypanel
- Revise as variáveis de ambiente
- Confirme a conexão com o banco de dados

## 📄 Licença

Desenvolvido para Grava Perfumes © 2026
