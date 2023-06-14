CREATE DATABASE users;
use users;

-- Tabela "Usuarios" no micro serviço "RegUser"
CREATE TABLE Usuarios (
  ID INT NOT NULL AUTO_INCREMENT,
  Nome VARCHAR(100),
  Email VARCHAR(100),
  Senha VARCHAR(100),
  PRIMARY KEY (ID)
);

INSERT INTO Usuarios (Nome, Email, Senha) VALUES ("Julio Machado", "julio.machado@pucrs.br", "Julio123");