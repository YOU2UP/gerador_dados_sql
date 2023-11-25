INSERT INTO usuario VALUES 
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Procuro alguém para treinar", "matheus@email.com", "Intermediário", 50, "Matheus Leal de Oliveira", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 1, 2),
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Programador java e maromba nas horas vagas", "vinicius@email.com", "Intermediário", 70, "Vinicius Cardoso", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 2, 2),
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Saúde e bem-estar, por isso eu treino!", "vitor@email.com", "Intermediário", 50, "Vitor Fernando", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 3, 2),
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Amante de esportes", "rafa@email.com", "Intermediário", 50, "Rafa", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 4, 2),
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Em busca do shape perfeito", "felipe@email.com", "Intermediário", 40, "Felipe Grossi", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 5, 2),
(null, STR_TO_DATE('2023-11-25 00:00:00', '%Y-%m-%d %H:%i:%s'), "2003-01-01", "Vamos treinar!?", "joao@email.com", "Intermediário", 80, "João", "$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC", 6, 2),

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