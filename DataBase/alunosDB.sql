CREATE DATABASE alunos;
use alunos;

-- Tabela Alunos
CREATE TABLE Alunos (
  Matricula INT PRIMARY KEY,
  Nome VARCHAR(255) NOT NULL,
  DocumentoIdentificacao INT NOT NULL,
  Endereco VARCHAR(255) NOT NULL
);


INSERT INTO Alunos (Matricula, Nome, DocumentoIdentificacao, Endereco) VALUES (0, "João", 123456789, "Rua A")
INSERT INTO Alunos (Matricula, Nome, DocumentoIdentificacao, Endereco) VALUES (1, "Maria", 987654321, "Rua 1")