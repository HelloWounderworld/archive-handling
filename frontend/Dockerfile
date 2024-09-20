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

# Instala o wget
RUN apt-get install -y wget

# Instala e o npm
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y npm

# Isso ira instalar o NodeJs usando o wget
WORKDIR /tmp
RUN wget https://nodejs.org/dist/v22.2.0/node-v22.2.0-linux-x64.tar.xz \
    && mkdir -p /usr/local/lib/nodejs \
    && tar -xJvf ./node-v22.2.0-linux-x64.tar.xz -C /usr/local/lib/nodejs

ENV PATH /usr/local/lib/nodejs/node-v22.2.0-linux-x64/bin:$PATH

# Verifica as versões instaladas
RUN node --version && npm --version

# Instala Vue CLI globalmente
RUN npm install -g @vue/cli

# Define o diretorio de trabalho para frontend
WORKDIR /frontend

# Copie todos os arquivos do projeto backend
COPY . /frontend/

# Tentando instalar as dependencias do package.json
RUN npm install

CMD ["npm", "run", "serve"]