CREATE DATABASE you2up;
USE you2up;

-- Tabela local_treino_usuario
CREATE TABLE local_treino_usuario (
    id_local_treino INTEGER PRIMARY KEY AUTO_INCREMENT,
    bairro  VARCHAR(255),
    cidade VARCHAR(255),
    is_academia BOOLEAN,
    nome VARCHAR(255),
    numero INTEGER,
    rua VARCHAR(255),
    uf VARCHAR(255)
);

-- SELECT * FROM usuario;

-- Tabela usuario
CREATE TABLE usuario (
    id_usuario INTEGER PRIMARY KEY AUTO_INCREMENT,
    data_criacao_conta TIMESTAMP,
    data_nascimento DATE,
    descricao VARCHAR(255),
    email VARCHAR(255),
    estagio VARCHAR(255),
    meta_treinos INTEGER,
    nome VARCHAR(255),
    senha VARCHAR(255),
    local_treino_id_local_treino INTEGER,
    FOREIGN KEY (local_treino_id_local_treino) REFERENCES local_treino_usuario(id_local_treino)
);

-- Tabela treino
CREATE TABLE treino (
    id_treino INTEGER PRIMARY KEY AUTO_INCREMENT,
    is_realizado BOOLEAN,
    periodo VARCHAR(255)
);

-- Tabela avaliacao
CREATE TABLE avaliacao (
    id_avaliacao INTEGER PRIMARY KEY AUTO_INCREMENT,
    nota DECIMAL(3,1),
    avaliado_id_usuario INTEGER,
    avaliador_id_usuario INTEGER,
    treino_id_treino INTEGER,
    FOREIGN KEY (avaliado_id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (avaliador_id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (treino_id_treino) REFERENCES treino(id_treino)
);

-- Tabela foto
CREATE TABLE foto (
    id_foto INTEGER PRIMARY KEY AUTO_INCREMENT,
    url VARCHAR(1000),
    usuario_id_usuario INTEGER,
    FOREIGN KEY (usuario_id_usuario) REFERENCES usuario(id_usuario)
);

-- Tabela foto_perfil
CREATE TABLE foto_perfil (
    id_foto_perfil INTEGER PRIMARY KEY AUTO_INCREMENT,
    url VARCHAR(1000),
    usuario_id_usuario INTEGER,
    FOREIGN KEY (usuario_id_usuario) REFERENCES usuario(id_usuario)
);

-- Tabela tb_match
CREATE TABLE tb_match (
    id_match INTEGER PRIMARY KEY AUTO_INCREMENT,
    data_match TIMESTAMP,
    is_ativo BOOLEAN,
    usuario1_id_usuario INTEGER,
    usuario2_id_usuario INTEGER,
    FOREIGN KEY (usuario1_id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (usuario2_id_usuario) REFERENCES usuario(id_usuario)
);

-- Tabela notificacao
CREATE TABLE notificacao (
    id_notificacao INTEGER PRIMARY KEY AUTO_INCREMENT,
    conteudo VARCHAR(255),
    data_hora TIMESTAMP,
    usuario_id_usuario INTEGER,
    FOREIGN KEY (usuario_id_usuario) REFERENCES usuario(id_usuario)
);

-- Tabela treino_has_usuario
CREATE TABLE treino_has_usuario (
    inicio_treino TIMESTAMP,
    treino_id_treino INTEGER,
    usuario_id_usuario INTEGER,
    PRIMARY KEY (inicio_treino, treino_id_treino, usuario_id_usuario),
    FOREIGN KEY (treino_id_treino) REFERENCES treino(id_treino),
    FOREIGN KEY (usuario_id_usuario) REFERENCES usuario(id_usuario)
);

USE you2up;
SELECT * FROM local_treino_usuario;
SELECT * FROM usuario;
SELECT * FROM treino;
SELECT * FROM avaliacao;
SELECT * FROM foto;
SELECT * FROM foto_perfil;	
SELECT * FROM tb_match;
SELECT * FROM notificacao;
SELECT * FROM treino_has_usuario;

SELECT * FROM usuario ORDER BY id_usuario DESC;
INSERT INTO usuario VALUES 
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Procuro alguém para treinar", "matheus@email.com", "Intermediário", 50, "Matheus Leal de Oliveira", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 1, 2),
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Programador java e maromba nas horas vagas", "vinicius@email.com", "Intermediário", 70, "Vinicius Cardoso", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 2, 2),
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Saúde e bem-estar, por isso eu treino!", "vitor@email.com", "Intermediário", 50, "Vitor Fernando", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 3, 2),
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Amante de esportes", "rafa@email.com", "Intermediário", 50, "Rafa", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 4, 2),
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Em busca do shape perfeito", "felipe@email.com", "Intermediário", 40, "Felipe Grossi", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 5, 2),
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Vamos treinar!?", "joao@email.com", "Intermediário", 80, "João", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 6, 2);

INSERT INTO treino VALUES 
(null, 0, "Manhã"),
(null, 1, "Tarde"),
(null, 1, "Noite"),
(null, 1, "Manhã"),
(null, 0, "Tarde"),
(null, 1, "Noite");

INSERT INTO treino_has_usuario VALUES
(STR_TO_DATE('2023-12-01 10:00:00', '%Y-%m-%d %H:%i:%s'), 53, 59),
(STR_TO_DATE('2023-11-24 15:30:00', '%Y-%m-%d %H:%i:%s'), 54, 59),
(STR_TO_DATE('2023-10-30 20:00:00', '%Y-%m-%d %H:%i:%s'), 55, 59),
(STR_TO_DATE('2023-11-23 09:00:00', '%Y-%m-%d %H:%i:%s'), 56, 59),
(STR_TO_DATE('2023-12-01 15:00:00', '%Y-%m-%d %H:%i:%s'), 57, 59),
(STR_TO_DATE('2023-11-22 21:30:00', '%Y-%m-%d %H:%i:%s'), 58, 59);

INSERT INTO avaliacao VALUES 
(null, 5.0, 59, 1, 54),
(null, 4.0, 59, 3, 55),
(null, 4.4, 59, 6, 56),
(null, 4.6, 59, 6, 58);