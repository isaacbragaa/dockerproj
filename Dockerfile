# Usa a imagem oficial do Python
FROM python:3.9

# Define o diretório de trabalho
WORKDIR /app

# Copia o requirements.txt e instala as dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia todas as aplicações para dentro do container
COPY containers /app/

# Define a variável de ambiente APP_DIR, que será usada para selecionar a aplicação
ARG APP_DIR
WORKDIR /app/${APP_DIR}

# Comando padrão para rodar a aplicação Flask
CMD ["python", "app.py"]
