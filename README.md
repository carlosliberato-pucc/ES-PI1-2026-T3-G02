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
- Leonardo Amad  
- Nicolas Reis

## 🌟 Projeto LAD.py - Sistema de Votação Digital

O **LAD.Py** é o backend de um sistema de votação digital fictício desenvolvido como Projeto Integrador I. O objetivo principal é integrar lógica de programação em Python, manipulação de bancos de dados relacionais (SQL) e conceitos de Álgebra Linear aplicados à segurança da informação.

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
  - `datetime` (Manipulação de logs e registros)
  - `random` (Geração de protocolos e chaves)
