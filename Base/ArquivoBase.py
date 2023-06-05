class Aluno ():
    def __init__(self,nome: str,numeroDoc: int,endereco: str,matricula: int):
        self.nome = nome
        self.numeroDoc = numeroDoc
        self.endereco = endereco
        self.matricula = matricula

class Disciplina ():
    def __init__(self, codigo: int,nome: str,horario: str,turma: int):
        self.codigo = codigo
        self.nome = nome
        self.horario = horario
        self.turma = turma

class MatriculaDisciplina ():
    def __init__(self, aluno: Aluno, disciplinas):
        self.aluno = aluno
        self.disciplinas = disciplinas

class User ():
    def __init__(self,nome: str,email: str,senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha
        
#-------------------------------------------------------------------------------------

matricula = 0
alunos = [Aluno]

def RegisterAluno (nome: str, numeroDoc: int, endereco: str):
    matricula = matricula + 1
    a = Aluno(nome, numeroDoc, endereco, matricula)
    #colocar no BD
    
def RegisterUser (nome: str, email: str, senha: str):
    a = User(nome, email, senha)
    #colocar no BD

def RegisterMatDisc (aluno: Aluno, disciplinas):
    a = MatriculaDisciplina(aluno, disciplinas)
    #colocar no BD

def RegisterDisciplina (codigo: int,nome: str, horario: str, turma: int):
    a = Disciplina(codigo, nome, horario, turma)
    #colocar no BD    
    
#-------------------------------------------------------------------------------------

def buscaTodosAlunos ():
    for aluno in alunos:
        print(aluno)

def buscaNomeAluno (parte: str):
    for aluno in alunos:
        for i in range(len(aluno.nome)-len(parte)):
            if(parte == aluno.nome[i,len(parte)]):
                print(aluno)

def buscaMatriculaAluno (mat: int):
    for aluno in alunos:
        if(mat == aluno.matricula):
            print(aluno)





