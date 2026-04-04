-- Desenvolvido por Carlos Liberato 1 hora
-- Criando Banco de dados LADPY
create database ladpy; 
use ladpy;

-- Criação da tabela eleitores com suas devidas informações
create table eleitores(
	id_eleitor int auto_increment primary key,
    nome_eleitor varchar(255) not null,
    cpf varchar(255) not null,
    titulo_eleitor varchar(12) not null,
    perfil ENUM('eleitor', 'mesario') not null default 'eleitor',
    chave_acesso varchar(255) not null,
    flag_voto boolean default FALSE,
    unique (titulo_eleitor),
    unique (cpf)
);

-- Criação da tabela candidados com suas devidas informações
create table candidatos(
	id_candidatos int primary key,
    nome_candidato varchar(255) not null,
    partido varchar(255) not null,
    cargo varchar(255) not null
);

-- Criação da tabela votos com suas devidas informações
create table votos(
	id_voto int auto_increment primary key,
    id_candidato int,
    data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    protocolo_confirmacao varchar(255),
	foreign key (id_candidato) references candidatos (id_candidatos)
);
