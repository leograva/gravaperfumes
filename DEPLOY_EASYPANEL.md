# 🚀 Guia de Deploy - Easypanel (Hostinger VPS)

## Passo a Passo Completo

### 1️⃣ Preparar o Código

```bash
# Criar repositório Git
git init
git add .
git commit -m "Deploy: Sistema Grava Perfumes"

# Criar repositório no GitHub
# Vá em github.com e crie um novo repositório
# Depois execute:
git remote add origin https://github.com/seu-usuario/gravaperfumes.git
git branch -M main
git push -u origin main
```

### 2️⃣ Acessar Easypanel

1. Acesse seu Easypanel: `https://seu-ip:3000` ou `https://painel.seu-dominio.com`
2. Faça login com suas credenciais

### 3️⃣ Criar Banco de Dados PostgreSQL

1. No Easypanel, clique em **"+ Create"**
2. Selecione **"Database"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `gravaperfumes-db`
   - **Database Name**: `gravaperfumes`
   - **Username**: `postgres`
   - **Password**: Crie uma senha forte (anote!)
4. Clique em **"Create"**
5. Aguarde o banco ser criado

### 4️⃣ Criar Aplicação Django

1. Clique em **"+ Create"** → **"App"**
2. Selecione **"From Source"** → **"GitHub"**
3. Conecte sua conta GitHub (se ainda não conectou)
4. Selecione o repositório `gravaperfumes`
5. Configure:

#### Build Settings:
- **Build Type**: `Dockerfile`
- **Dockerfile Path**: `Dockerfile`

#### General Settings:
- **Name**: `gravaperfumes`
- **Port**: `8000`

### 5️⃣ Configurar Variáveis de Ambiente

Na seção **"Environment Variables"**, adicione:

```env
SECRET_KEY=cole-aqui-uma-chave-secreta-forte-gerada
DEBUG=False
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com,seu-ip-vps

# Database (use os dados do PostgreSQL criado)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=gravaperfumes
DB_USER=postgres
DB_PASSWORD=a-senha-que-voce-criou
DB_HOST=gravaperfumes-db
DB_PORT=5432
```

**Para gerar SECRET_KEY**, use:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 6️⃣ Conectar App ao Banco

1. Nas configurações do app, vá em **"Links"**
2. Clique em **"Add Link"**
3. Selecione o banco `gravaperfumes-db`
4. Isso criará automaticamente as variáveis de conexão

### 7️⃣ Deploy

1. Clique em **"Deploy"**
2. Aguarde o build (pode levar 2-5 minutos)
3. Acompanhe os logs para ver o progresso

### 8️⃣ Executar Migrações

Após o deploy bem-sucedido:

1. Vá em **"Console"** ou **"Terminal"** do app
2. Execute os comandos:

```bash
# Migrar banco de dados
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
# Siga as instruções para criar usuário e senha

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# (Opcional) Popular dados de exemplo
python popular_dados.py
```

### 9️⃣ Configurar Domínio

1. No Easypanel, vá em **"Domains"** do seu app
2. Clique em **"Add Domain"**
3. Digite seu domínio: `gravaperfumes.com.br`
4. O Easypanel configurará SSL automaticamente (Let's Encrypt)

#### Configurar DNS:

No painel da Hostinger ou seu provedor de domínio:

```
Tipo: A
Nome: @
Valor: IP-DA-SUA-VPS

Tipo: A
Nome: www
Valor: IP-DA-SUA-VPS
```

Aguarde propagação DNS (pode levar até 24h, geralmente 1-2h)

### 🔟 Testar o Sistema

1. Acesse: `https://seu-dominio.com`
2. Você verá a tela de login
3. Entre com o superusuário criado
4. Pronto! Sistema no ar! 🎉

## 📋 Checklist de Deploy

- [ ] Código no GitHub
- [ ] PostgreSQL criado no Easypanel
- [ ] App criado e conectado ao banco
- [ ] Variáveis de ambiente configuradas
- [ ] Deploy realizado com sucesso
- [ ] Migrações executadas
- [ ] Superusuário criado
- [ ] Domínio configurado
- [ ] SSL ativo
- [ ] Login funcionando

## 🔧 Comandos Úteis

### Ver Logs
```bash
# No Easypanel, vá em "Logs" do app
# Ou no terminal:
docker logs -f nome-do-container
```

### Reiniciar App
```bash
# No Easypanel, clique em "Restart"
```

### Backup do Banco
```bash
# No terminal do PostgreSQL:
pg_dump gravaperfumes > backup.sql
```

### Restaurar Banco
```bash
psql gravaperfumes < backup.sql
```

## 🐛 Troubleshooting

### Erro: "Bad Gateway"
- Verifique se o app está rodando
- Confira os logs
- Verifique a porta (deve ser 8000)

### Erro: "Database connection failed"
- Verifique as variáveis DB_*
- Confirme que o PostgreSQL está rodando
- Teste a conexão no terminal

### Erro: "Static files not found"
- Execute: `python manage.py collectstatic --noinput`
- Verifique STATIC_ROOT nas configurações

### Erro: "ALLOWED_HOSTS"
- Adicione seu domínio em ALLOWED_HOSTS
- Formato: `dominio.com,www.dominio.com`

## 📊 Monitoramento

### Verificar Status
- Easypanel Dashboard mostra CPU, RAM e Disco
- Logs em tempo real disponíveis

### Backup Automático
Configure backup automático do PostgreSQL no Easypanel:
1. Vá em configurações do banco
2. Ative "Automated Backups"
3. Escolha frequência (diário recomendado)

## 🔒 Segurança

### Após Deploy:
1. ✅ Mude SECRET_KEY
2. ✅ Use senha forte no banco
3. ✅ Ative SSL (automático no Easypanel)
4. ✅ Configure firewall na VPS
5. ✅ Mantenha Django atualizado

## 📞 Suporte

Se tiver problemas:
1. Verifique os logs no Easypanel
2. Revise as variáveis de ambiente
3. Confirme conexão com banco de dados
4. Teste localmente primeiro

## 🎉 Pronto!

Seu sistema está no ar e pronto para uso!

Acesse: `https://seu-dominio.com`
