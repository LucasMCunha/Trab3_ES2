CREATE DATABASE disciplinas;
use disciplinas;

-- Tabela Disciplinas
CREATE TABLE Disciplinas (
  CodigoDisciplina INT NOT NULL,
  NomeDisciplina VARCHAR(100),
  HorarioDisciplina VARCHAR(50),
  Turma INT NOT NULL,
  PRIMARY KEY (CodigoDisciplina, Turma)
);

-- Inserir uma nova disciplina
INSERT INTO Disciplinas (CodigoDisciplina, NomeDisciplina, HorarioDisciplina, Turma) VALUES (0, "Fundamentos de Proagramação", "AB", 10);
INSERT INTO Disciplinas (CodigoDisciplina, NomeDisciplina, HorarioDisciplina, Turma) VALUES (0, "Fundamentos de Proagramação", "CD", 11);
INSERT INTO Disciplinas (CodigoDisciplina, NomeDisciplina, HorarioDisciplina, Turma) VALUES (1, "Métodos Numéricos", "JK", 30);
INSERT INTO Disciplinas (CodigoDisciplina, NomeDisciplina, HorarioDisciplina, Turma) VALUES (1, "Métodos Numéricos", "LM", 31);