FROM python:3.11-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do projeto
COPY . .

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Criar diretório para mídia
RUN mkdir -p /app/media

# Expor porta
EXPOSE 8000

# Script de inicialização
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Comando para iniciar o servidor
CMD ["/app/start.sh"]
