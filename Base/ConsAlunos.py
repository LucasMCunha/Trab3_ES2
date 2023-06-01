import RegAlunos

alunos = [RegAlunos.Aluno]

def buscaTodos ():
    for aluno in alunos:
        print(aluno)

def buscaNome (parte: str):
    for aluno in alunos:
        for i in range(len(aluno.nome)-len(parte)):
            if(parte == aluno.nome[i,len(parte)]):
                print(aluno)

def buscaMatricula (mat: int):
    for aluno in alunos:
        if(mat == aluno.matricula):
            print(aluno)

