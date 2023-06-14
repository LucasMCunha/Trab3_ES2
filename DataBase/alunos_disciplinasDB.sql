-- Tabela Matriculas
CREATE DATABASE alunosDisciplinas;
use alunosDisciplinas;

CREATE TABLE Matriculas (
  Id INT NOT NULL AUTO_INCREMENT,
  AlunoMatricula INT NOT NULL,
  DisciplinaCodigo INT NOT NULL,
  DisciplinaTurma INT NOT NULL,
  PRIMARY KEY (Id)
);

INSERT INTO Matriculas (AlunoMatricula, DisciplinaCodigo, DisciplinaTurma) VALUES (0, 0, 10);
INSERT INTO Matriculas (AlunoMatricula, DisciplinaCodigo, DisciplinaTurma) VALUES (1, 0, 10);
INSERT INTO Matriculas (AlunoMatricula, DisciplinaCodigo, DisciplinaTurma) VALUES (0, 1, 30);
INSERT INTO Matriculas (AlunoMatricula, DisciplinaCodigo, DisciplinaTurma) VALUES (1, 1, 31);


