CREATE DATABASE disciplinas;
use disciplinas;

-- Tabela "Disciplinas" no micro serviço "RegDisciplinas"
CREATE TABLE Disciplinas (
  CodigoDisciplina INT PRIMARY KEY,
  NomeDisciplina VARCHAR(100),
  HorarioDisciplina VARCHAR(50),
  Turma INT
);