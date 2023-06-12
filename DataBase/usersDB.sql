CREATE DATABASE users;
use users;

-- Tabela "Usuarios" no micro serviço "RegUser"
CREATE TABLE Usuarios (
  ID INT PRIMARY KEY,
  Email VARCHAR(100),
  Nome VARCHAR(100),
  Senha VARCHAR(100)
);

