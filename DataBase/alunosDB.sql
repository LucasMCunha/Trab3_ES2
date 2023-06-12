CREATE DATABASE alunos;
use alunos;

-- Tabela "Alunos" no micro serviço "RegAlunos"
CREATE TABLE Alunos (
  Matricula INT PRIMARY KEY,
  Nome VARCHAR(100),
  DocumentoIdentificacao INT,
  Endereco VARCHAR(200)
);