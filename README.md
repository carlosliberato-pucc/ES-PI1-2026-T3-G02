# 📘 Projeto Integrador I – Engenharia de Software  

## 📌 Informações Gerais
- **Disciplina:** Projeto Integrador I
- **Curso:** Engenharia de Software  
- **Semestre:** 2026/1
- **Turma:** T3  
- **Grupo:** G2  
- **Professor:** Luã Marcelo Muriana  

## 👨‍💻 Integrantes do Grupo
- Bruno Terra
- Carlos Liberato  
- Felipe Miranda  
- Gabriel Coutinho  
- Nicolas Reis

## 🌟 Projeto LAD.py - Sistema de Votação Digital

O **LAD.Py** é um sistema de votação digital fictício desenvolvido como Projeto Integrador I. O objetivo principal é integrar lógica de programação em Python, manipulação de bancos de dados relacionais (SQL) e conceitos de Álgebra Linear aplicados à segurança da informação.

## 📌 Visão Geral

O sistema simula um ambiente de votação eletrônica focado em segurança e integridade, permitindo o gerenciamento de eleitores, candidatos e o processamento sigiloso de votos através de uma interface de linha de comando.

### Principais Funcionalidades
- **Módulo de Gerenciamento:** CRUD (Create, Read, Update, Delete) de eleitores e candidatos.
- **Validação de Documentos:** Implementação algorítmica para validação de CPF e Título de Eleitor.
- **Módulo de Votação:** Interface para identificação do eleitor, escolha de candidatos e confirmação de voto.
- **Segurança (Cifra de Hill):** Proteção de dados sensíveis como chaves de acesso, protocolos e CPFs utilizando matrizes e criptografia.
- **Auditoria e Transparência:** Geração de arquivos de log (.txt) para eventos do sistema e emissão de Zerézima.

## 🛠️ Tecnologias e Requisitos

- **Linguagem:** Python 3.x
- **Banco de Dados:** MySQL
- **Dependências Necessárias:**
  - `mysql-connector-python` (Conexão com o banco de dados)

---

## 🚀 Como Rodar Localmente (Guia Rápido)

### 📋 Pré-requisitos

Antes de começar, você precisa ter instalado:

1. **MySQL Server** (versão 8.0 ou superior) - [Download aqui](https://dev.mysql.com/downloads/mysql/)
2. **Git** - [Download aqui](https://git-scm.com/)

---

## 🗄️ PASSO 1: Instalar e Configurar o MySQL

### 1.1. Instalar o MySQL Server

1. Baixe o **MySQL Installer** no site oficial: https://dev.mysql.com/downloads/installer/
2. Execute o instalador e escolha a opção **"Developer Default"** ou **"Server only"**
3. Durante a instalação:
   - Defina uma **senha root** (anote essa senha!)
   - Mantenha a porta padrão **3306**
   - Configure para iniciar o MySQL automaticamente
4. Finalize a instalação

### 1.2. Verificar se o MySQL está Rodando

Abra o **Prompt de Comando (CMD)** ou **PowerShell** e execute:

```bash
mysql --version
```

Se aparecer a versão do MySQL, está instalado corretamente! 

Caso contrário, adicione o MySQL ao PATH do Windows:
- Procure por "Variáveis de Ambiente" no menu Iniciar
- Em "Path" do sistema, adicione: `C:\Program Files\MySQL\MySQL Server 8.0\bin`

### 1.3. Criar o Banco de Dados NotaDez

Existem **duas formas** de criar o banco de dados:

---

#### **OPÇÃO A: Via MySQL Workbench (Mais Fácil - RECOMENDADO)**

1. Abra o **MySQL Workbench** (instalado junto com o MySQL)
2. Clique em **"Local instance MySQL80"** e digite a senha root
3. No painel central, cole o seguinte comando:

```sql
CREATE DATABASE ladpy;
```

4. Clique no ícone de **raio ⚡** para executar (ou pressione `Ctrl + Enter`)
5. No menu lateral esquerdo, clique com botão direito em **Schemas** → **Refresh All**
6. Você verá o banco `ladpy` aparecer na lista
7. Execute o comando abaixo para selecionar o banco:

```sql
USE ladpy;
```

8. Agora, abra o arquivo `LADPY.sql` que está na pasta do projeto:
   - Clique em **File → Open SQL Script**
   - Navegue até a pasta do projeto e selecione `LADPY.sql`
   - Clique no ícone de **raio ⚡** para executar TODO o script de uma vez
   - Aguarde até aparecer "X statements executed successfully"

9. Pronto! Todas as tabelas e triggers foram criadas automaticamente.

---

### 1.4. Verificar se as Tabelas Foram Criadas

No **MySQL Workbench** ou via **linha de comando**, execute:

```sql
USE ladpy;
SHOW TABLES;
```

Se todas aparecerem, o banco está configurado corretamente! ✅

---

## 💻 PASSO 2: Clonar e Configurar o Projeto
## 2.1. Instalar o Git
Baixe no [site oficial](https://git-scm.com/) e instale normalmente. Na instalação, mantenha as opções padrão.

Após instalar, feche e abra novamente o terminal para garantir que git já funciona.
### 2.2. Clonar o Repositório

Abra o **CMD** ou **PowerShell** e execute:

```bash
git clone https://github.com/carlosliberato-pucc/ES-PI1-2026-T3-G02.git
cd ES-PI1-2026-T3-G02
```

### 2.2. Configurar as Variáveis de Ambiente (.env)

1. Na pasta do projeto, abra o arquivo `database/conexao.py` em um editor de texto (Bloco de Notas, VSCode, etc)
2. Preencha as informações do MySQL que você configurou:

```env
# Configurações do Banco de Dados MySQL
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "sua_senha_root_aqui",
        database = "ladpy"
    )
```

**IMPORTANTE:** Substitua `sua_senha_root_aqui` pela senha que você definiu quando instalou o MySQL!

4. Salve o arquivo `conexao.py`

---

## 📦 PASSO 3: Instalar Dependências do Projeto

No CMD/PowerShell (dentro da pasta do projeto), execute:

**Opção 1:** O jeito padrão (Tente este primeiro)
Digite o comando abaixo e aperte Enter:

```powershell
pip install mysql-connector-python
```

**Opção 2:** Se a Opção 1 der erro de "comando não encontrado"
Se o computador disser que não reconhece a palavra "pip", significa que o Python precisa de uma ajudinha para se achar. Use este comando:

```powershell
python -m pip install mysql-connector-python
```
**O que fazer agora?**
Aguarde: Algumas linhas de texto vão começar a correr na tela. É normal! Espera até que elas parem e o símbolo > apareça de novo.

Mensagem de sucesso: Se no final aparecer algo como “Successfully installed...”, deu tudo certo!
---

## 🚀 PASSO 4: Colocar o Projeto para Rodar!

Com tudo instalado, chegou a hora de ver o seu projeto ladpy funcionando na prática.

No mesmo terminal (CMD ou PowerShell) onde você instalou as dependências, digite o comando abaixo e aperte Enter:

```powershell
python main.py
```
❓ **E se der erro? Veja como resolver:**
Erro de **"Arquivo não encontrado"** (No such file or directory): Isso significa que o terminal não está "enxergando" o arquivo main.py. Garanta que você está na pasta certa do projeto.

Erro de **"Comando não encontrado"** (python não é reconhecido): Se o computador reclamar da palavra python, tente trocar por py ou python3, assim:

```powershell
py main.py
```

🎉 Como saber se deu certo?
Se o programa abrir, começar a mostrar mensagens do seu sistema ou não der nenhuma mensagem de erro vermelha, parabéns! O seu projeto já está rodando.
---
