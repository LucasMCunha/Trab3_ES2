
class Disciplina ():
    def __init__(self, codigo: int,nome: str,horario: str,turma: int):
        self.codigo = codigo
        self.nome = nome
        self.horario = horario
        self.turma = turma



def Register (codigo: int,nome: str, horario: str, turma: int):
    a = Disciplina(codigo, nome, horario, turma)
    #colocar no BD