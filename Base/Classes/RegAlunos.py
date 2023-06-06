from flask import Flask, request, jsonify

app = Flask(__name__)
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

@app.route('/aluno', methods=['POST'])
def aluno():
    if request.method == "POST":
        req = request.args
        name = req['name']
        numId= req['number ID']
        add = req['address']
        return jsonify({"response": f"Post Request Called. Name: {name}, Number of ID: {numId}, Address: {add}"})
 
if __name__ == '__main__':
    app.run(debug=True, port=9090)