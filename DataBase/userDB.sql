CREATE DATABASE users;
use users;

-- Tabela "Usuarios" no micro serviço "RegUser"
CREATE TABLE Usuarios (
  ID INT PRIMARY KEY,
  Nome VARCHAR(100),
  Email VARCHAR(100),
  Senha VARCHAR(100)
);

INSERT INTO Alunos (ID, Nome, Email, Senha) VALUES (0, "Julio Machado", "julio.machado@pucrs.br", "Julio123")