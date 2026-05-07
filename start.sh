#!/bin/bash

echo "🚀 Iniciando Grava Perfumes..."

# Aguardar banco de dados estar pronto
echo "⏳ Aguardando banco de dados..."
sleep 5

# Executar migrações
echo "📦 Executando migrações..."
python manage.py migrate --noinput

# Coletar arquivos estáticos
echo "📁 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Iniciar Gunicorn
echo "✅ Iniciando servidor..."
gunicorn --bind 0.0.0.0:8000 --workers 3 --timeout 120 gravaperfumes.wsgi:application
