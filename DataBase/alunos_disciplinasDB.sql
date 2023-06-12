CREATE DATABASE alunos_disciplinas;
use alunos_disciplinas;

-- Tabela "Matriculas" no micro serviço "RegMatDisci"
CREATE TABLE Matriculas (
  Matricula INT,
  CodigoDisciplina INT,
  PRIMARY KEY (Matricula, CodigoDisciplina),
  FOREIGN KEY (Matricula) REFERENCES Alunos(Matricula),
  FOREIGN KEY (CodigoDisciplina) REFERENCES Disciplinas(CodigoDisciplina)
);