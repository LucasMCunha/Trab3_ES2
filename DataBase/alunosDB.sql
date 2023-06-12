CREATE DATABASE alunos;
use alunos;

-- Tabela "Alunos" no micro serviço "RegAlunos"
CREATE TABLE Alunos (
  Matricula INT PRIMARY KEY,
  Nome VARCHAR(100),
  DocumentoIdentificacao VARCHAR(20),
  Endereco VARCHAR(200)
);