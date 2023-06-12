-- Tabela Matriculas
CREATE DATABASE alunosDisciplinas;
use alunosDisciplinas;

CREATE TABLE Matriculas (
  Id INT PRIMARY KEY,
  AlunoMatricula INT NOT NULL,
  DisciplinaCodigo INT NOT NULL,
  DisciplinaTurma INT NOT NULL,
  FOREIGN KEY (AlunoMatricula) REFERENCES Alunos (Matricula),
  FOREIGN KEY (DisciplinaCodigo, DisciplinaTurma) REFERENCES Disciplinas (CodigoDisciplina, Turma)
);

INSERT INTO Matriculas (Id, AlunoId, DisciplinaId, DisciplinaTurma) VALUES (0, 0, 0, 10)
INSERT INTO Matriculas (Id, AlunoId, DisciplinaId, DisciplinaTurma) VALUES (1, 1, 0, 10)
INSERT INTO Matriculas (Id, AlunoId, DisciplinaId, DisciplinaTurma) VALUES (2, 0, 1, 30)
INSERT INTO Matriculas (Id, AlunoId, DisciplinaId, DisciplinaTurma) VALUES (3, 1, 1, 31)