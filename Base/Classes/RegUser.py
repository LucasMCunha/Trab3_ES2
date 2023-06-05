class User ():
    def __init__(self,nome: str,email: str,senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha


def Register (nome: str, email: str, senha: str):
    a = User(nome, email, senha)
    #colocar no BD
