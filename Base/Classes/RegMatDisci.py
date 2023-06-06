import RegDisciplinas
import RegAlunos
import ConsAlunos

class MatriculaDisciplina ():
    def __init__(self, aluno: RegAlunos.Aluno, disciplinas):
        self.aluno = aluno
        self.disciplinas = disciplinas

def Register (aluno: RegAlunos.Aluno, disciplinas):
    a = MatriculaDisciplina(aluno, disciplinas)
    #colocar no BD
    
def getDiscAluno(aluno: RegAlunos.Aluno):
    if ConsAlunos.buscaAluno(aluno) != None:
        #pegar lista de disciplinas do banco a partir do nome do aluno
        for d in RegDisciplinas:
            print(d)

def getAlunosDisc(disciplina: RegDisciplinas.Disciplina):
    #pegar na base de dados todos os alunos
    for a in RegAlunos:
        print(a)
