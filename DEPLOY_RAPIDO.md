# ⚡ Deploy Rápido - Easypanel

## 🎯 Resumo em 5 Passos

### 1. GitHub
```bash
git init
git add .
git commit -m "Deploy Grava Perfumes"
git remote add origin https://github.com/SEU-USUARIO/gravaperfumes.git
git push -u origin main
```

### 2. Easypanel - Criar PostgreSQL
- **+ Create** → **Database** → **PostgreSQL**
- Name: `gravaperfumes-db`
- Database: `gravaperfumes`
- User: `postgres`
- Password: `[SENHA-FORTE]` ← **ANOTE!**

### 3. Easypanel - Criar App
- **+ Create** → **App** → **GitHub**
- Repositório: `gravaperfumes`
- Build: **Dockerfile**
- Port: **8000**

### 4. Variáveis de Ambiente
```env
SECRET_KEY=[GERAR-CHAVE-SECRETA]
DEBUG=False
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
DB_ENGINE=django.db.backends.postgresql
DB_NAME=gravaperfumes
DB_USER=postgres
DB_PASSWORD=[SENHA-DO-PASSO-2]
DB_HOST=gravaperfumes-db
DB_PORT=5432
```

**Gerar SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Deploy e Configurar
```bash
# Após deploy, no terminal do Easypanel:
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

## 🌐 Configurar Domínio

### No Easypanel:
- **Domains** → **Add Domain** → `seu-dominio.com`

### No DNS (Hostinger):
```
Tipo: A | Nome: @ | Valor: [IP-VPS]
Tipo: A | Nome: www | Valor: [IP-VPS]
```

## ✅ Pronto!

Acesse: `https://seu-dominio.com`

---

📖 **Guia completo**: Veja `DEPLOY_EASYPANEL.md`
