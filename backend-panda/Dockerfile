# Definindo a distribuicao que quero utilizar no meu container
FROM ubuntu:22.04

# Vamos definir o shell padrao, de forma segura, que e representado pelo "-c"
SHELL ["/bin/bash", "-c"]

# Vamos automatizar algumas construcoes e instalacoes de pacotes do Ubuntu, de forma nao interativa
ARG DEBIAN_FRONTEND=noninteractive

# Atualiza os pacotes do sistema
RUN apt-get update && apt-get upgrade -y

# Install text editor
RUN apt-get install nano

# Install request tool
RUN apt-get install -y curl

# Instala o Python 3 e pip
RUN apt-get install -y python3 python3-pip

# Verifica a versão do Python
RUN python3 --version

# Define o diretorio de trabalho para backend
WORKDIR /backend-panda

# Copiando do meu diretorio local para o diretorio do container
COPY ./requirements.txt /backend-panda

# Instale as bibliotecas Python
RUN apt-get install -y python3.10-venv
RUN python3 -m venv .venv
RUN source .venv/bin/activate
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /backend-panda/requirements.txt

# Copie todos os arquivos do projeto backend
COPY . /backend-panda/

# Congela as bibliotecas que foi instalado
RUN python3 -m pip freeze > requirements.txt

# Define o comando padrão para executar a aplicação
CMD ["uvicorn", "main":app", "--host", "0.0.0.0", "--port", "3000"]