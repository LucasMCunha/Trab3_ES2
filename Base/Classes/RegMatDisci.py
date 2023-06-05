import RegDisciplinas
import RegAlunos

class MatriculaDisciplina ():
    def __init__(self, aluno: RegAlunos.Aluno, disciplinas):
        self.aluno = aluno
        self.disciplinas = disciplinas



def Register (aluno: RegAlunos.Aluno, disciplinas):
    a = MatriculaDisciplina(aluno, disciplinas)
    #colocar no BD
