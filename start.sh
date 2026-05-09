#!/bin/sh

echo "Aguardando banco de dados..."
sleep 5

echo "Executando migracoes..."
python manage.py migrate --noinput

echo "Coletando arquivos estaticos..."
python manage.py collectstatic --noinput

echo "Iniciando servidor Gunicorn..."
exec gunicorn gravaperfumes.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --timeout 120 \
    --log-level info \
    --access-logfile - \
    --error-logfile -
