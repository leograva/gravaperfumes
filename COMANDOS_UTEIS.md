# 🛠️ Comandos Úteis - Grava Perfumes

## 🚀 Deploy

### Enviar para GitHub
```bash
git add .
git commit -m "Atualização do sistema"
git push
```

### Redesploy no Easypanel
No painel do Easypanel, clique em **"Redeploy"**

## 🗄️ Banco de Dados

### Criar Migrações
```bash
python manage.py makemigrations
```

### Aplicar Migrações
```bash
python manage.py migrate
```

### Resetar Banco (CUIDADO!)
```bash
python manage.py flush
```

### Backup do Banco
```bash
# PostgreSQL
pg_dump gravaperfumes > backup_$(date +%Y%m%d).sql

# SQLite
cp db.sqlite3 backup_$(date +%Y%m%d).sqlite3
```

### Restaurar Banco
```bash
# PostgreSQL
psql gravaperfumes < backup.sql

# SQLite
cp backup.sqlite3 db.sqlite3
```

## 👤 Usuários

### Criar Superusuário
```bash
python manage.py createsuperuser
```

### Alterar Senha
```bash
python manage.py changepassword admin
```

### Listar Usuários
```bash
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()
```

## 📁 Arquivos Estáticos

### Coletar Estáticos
```bash
python manage.py collectstatic --noinput
```

### Limpar Estáticos
```bash
rm -rf staticfiles/
python manage.py collectstatic --noinput
```

## 🧪 Testes

### Rodar Servidor Local
```bash
python manage.py runserver
```

### Rodar em Porta Diferente
```bash
python manage.py runserver 8080
```

### Acessar Shell Django
```bash
python manage.py shell
```

## 📊 Dados

### Popular Dados de Exemplo
```bash
python popular_dados.py
```

### Exportar Dados
```bash
python manage.py dumpdata perfumes > dados.json
```

### Importar Dados
```bash
python manage.py loaddata dados.json
```

## 🔍 Debug

### Ver Logs (Easypanel)
No painel, vá em **"Logs"** do app

### Ver Logs (Docker)
```bash
docker logs -f container-name
```

### Verificar Configurações
```bash
python manage.py check
```

### Verificar Deploy
```bash
python manage.py check --deploy
```

## 🔐 Segurança

### Gerar SECRET_KEY
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Verificar Permissões
```bash
python manage.py check --deploy
```

## 📦 Dependências

### Instalar Dependências
```bash
pip install -r requirements.txt
```

### Atualizar Dependências
```bash
pip list --outdated
pip install --upgrade nome-pacote
pip freeze > requirements.txt
```

## 🐳 Docker

### Build Local
```bash
docker build -t gravaperfumes .
```

### Rodar Local
```bash
docker run -p 8000:8000 gravaperfumes
```

### Ver Containers
```bash
docker ps
```

### Parar Container
```bash
docker stop container-id
```

## 🌐 Domínio

### Verificar DNS
```bash
nslookup seu-dominio.com
```

### Testar SSL
```bash
curl -I https://seu-dominio.com
```

## 📊 Estatísticas

### Contar Registros
```bash
python manage.py shell
>>> from perfumes.models import *
>>> print(f"Clientes: {Cliente.objects.count()}")
>>> print(f"Perfumes: {Perfume.objects.count()}")
>>> print(f"Vendas: {Venda.objects.count()}")
```

### Ver Últimas Vendas
```bash
python manage.py shell
>>> from perfumes.models import Venda
>>> Venda.objects.order_by('-data_venda')[:5]
```

## 🔄 Manutenção

### Limpar Sessões Expiradas
```bash
python manage.py clearsessions
```

### Otimizar Banco
```bash
# PostgreSQL
python manage.py dbshell
>>> VACUUM ANALYZE;
```

## 📝 Logs

### Ver Logs de Erro
```bash
tail -f logs/error.log
```

### Limpar Logs
```bash
> logs/error.log
```

## 🚨 Emergência

### Modo Manutenção
Crie arquivo `maintenance.html` e configure no Easypanel

### Rollback
```bash
git revert HEAD
git push
# Redesploy no Easypanel
```

### Restaurar Backup
```bash
# Parar app
# Restaurar banco
psql gravaperfumes < backup.sql
# Reiniciar app
```

## 💡 Dicas

### Verificar Variáveis de Ambiente
```bash
python manage.py shell
>>> import os
>>> print(os.environ.get('DEBUG'))
>>> print(os.environ.get('ALLOWED_HOSTS'))
```

### Testar Email (se configurado)
```bash
python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Teste', 'Mensagem', 'from@example.com', ['to@example.com'])
```

### Performance
```bash
# Ver queries lentas
python manage.py shell
>>> from django.db import connection
>>> print(connection.queries)
```

---

## 📞 Ajuda Rápida

**Erro 500**: Verifique logs e DEBUG=True temporariamente
**Erro 404**: Verifique URLs e ALLOWED_HOSTS
**Erro de Banco**: Verifique variáveis DB_*
**Estáticos não carregam**: Execute collectstatic

---

**Mantenha este arquivo como referência!**
