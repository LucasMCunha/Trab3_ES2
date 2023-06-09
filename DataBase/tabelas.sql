-- Tabela "Alunos" no micro serviço "RegAlunos"
CREATE TABLE Alunos (
  Matricula INT PRIMARY KEY,
  Nome VARCHAR(100),
  DocumentoIdentificacao VARCHAR(20),
  Endereco VARCHAR(200)
);

-- Tabela "Disciplinas" no micro serviço "RegDisciplinas"
CREATE TABLE Disciplinas (
  CodigoDisciplina INT PRIMARY KEY,
  NomeDisciplina VARCHAR(100),
  HorarioDisciplina VARCHAR(50),
  Turma VARCHAR(50)
);

-- Tabela "Matriculas" no micro serviço "RegMatDisci"
CREATE TABLE Matriculas (
  Matricula INT,
  CodigoDisciplina INT,
  PRIMARY KEY (Matricula, CodigoDisciplina),
  FOREIGN KEY (Matricula) REFERENCES Alunos(Matricula),
  FOREIGN KEY (CodigoDisciplina) REFERENCES Disciplinas(CodigoDisciplina)
);

-- Tabela "Usuarios" no micro serviço "RegUser"
CREATE TABLE Usuarios (
  ID INT PRIMARY KEY,
  Email VARCHAR(100),
  Nome VARCHAR(100),
  Senha VARCHAR(100)
);
