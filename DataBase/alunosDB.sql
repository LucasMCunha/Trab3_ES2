CREATE DATABASE alunos;
use alunos;

-- Tabela Alunos
CREATE TABLE Alunos (
  Matricula INT NOT NULL AUTO_INCREMENT,
  Nome VARCHAR(255) NOT NULL,
  DocumentoIdentificacao INT NOT NULL,
  Endereco VARCHAR(255) NOT NULL,
  PRIMARY KEY (Matricula)
);


-- INSERT INTO Alunos (Matricula, Nome, DocumentoIdentificacao, Endereco) VALUES (0, "João", 123456789, "Rua A");
-- INSERT INTO Alunos (Matricula, Nome, DocumentoIdentificacao, Endereco) VALUES (1, "Maria", 987654321, "Rua 1");

INSERT INTO Alunos (Nome, DocumentoIdentificacao, Endereco) VALUES ("João", 123456789, "Rua A");
INSERT INTO Alunos (Nome, DocumentoIdentificacao, Endereco) VALUES ("Maria", 987654321, "Rua 1");
