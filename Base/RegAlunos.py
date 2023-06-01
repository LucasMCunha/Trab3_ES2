matricula = 0

class Aluno ():
    def __init__(self,nome: str,numeroDoc: int,endereco: str,matricula: int):
        self.nome = nome
        self.numeroDoc = numeroDoc
        self.endereco = endereco
        self.matricula = matricula



def Register (nome: str, numeroDoc: int, endereco: str):
    matricula = matricula + 1
    a = Aluno(nome, numeroDoc, endereco, matricula)
    #colocar no BD



