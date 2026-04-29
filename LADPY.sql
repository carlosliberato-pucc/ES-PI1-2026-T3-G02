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
	id_candidato int primary key,
    nome_candidato varchar(255) not null,
    partido varchar(255) not null,
    cargo varchar(255) not null
);

INSERT INTO candidatos (id_candidato, nome_candidato, partido, cargo) VALUES
-- PRESIDENTE (ID com 2 dígitos)
(15, 'Dra. Beatriz Albuquerque', 'MDB', 'Presidente'),
(22, 'Marcos Vinícius "O Reformador"', 'PL', 'Presidente'),

-- GOVERNADOR (ID com 2 dígitos)
(10, 'Engenheiro Paulo Guedes', 'REPUBLICANOS', 'Governador'),
(13, 'Professora Sônia', 'PT', 'Governador'),

-- SENADOR (ID com 3 dígitos)
(151, 'Comandante Castro', 'MDB', 'Senador'),
(222, 'Dona Dirce da Saúde', 'PL', 'Senador'),
(455, 'Ricardo Menezes', 'PSDB', 'Senador'),

-- DEPUTADO FEDERAL (ID com 4 dígitos)
(1010, 'Felipe Tech', 'REPUBLICANOS', 'Deputado Federal'),
(1313, 'Pastora Célia', 'PT', 'Deputado Federal'),
(2020, 'Beto do Sindicato', 'PODE', 'Deputado Federal'),

-- DEPUTADO ESTADUAL (ID com 5 dígitos)
(10123, 'Zezinho do Bairro', 'REPUBLICANOS', 'Deputado Estadual'),
(15789, 'Doutor Renato', 'MDB', 'Deputado Estadual'),
(45000, 'Clara das Causas Sociais', 'PSDB', 'Deputado Estadual');

-- Criação da tabela votos com suas devidas informações
create table votos(
	id_voto int auto_increment primary key,
    id_candidato int,
    data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    protocolo_confirmacao varchar(255),
	foreign key (id_candidato) references candidatos (id_candidatos)
);
