# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do aplicativo para o diretório de trabalho
COPY . .

# Exponha a porta que o Flask usará
EXPOSE 5001

# Defina a variável de ambiente para garantir que os logs do Flask apareçam no console do Docker
ENV FLASK_ENV=production

# Comando para rodar o aplicativo Flask
CMD ["python", "api.py"]
