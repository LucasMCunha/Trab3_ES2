from flask import Flask, request, jsonify

app = Flask(__name__)

class Disciplina ():
    def __init__(self, codigo: int,nome: str,horario: str,turma: int):
        self.codigo = codigo
        self.nome = nome
        self.horario = horario
        self.turma = turma



def Register (codigo: int,nome: str, horario: str, turma: int):
    a = Disciplina(codigo, nome, horario, turma)
    #colocar no BD
    
@app.route('/disc', methods=['POST'])
def disciplina():
    if request.method == "POST":
        req = request.args
        name = req['name']
        return jsonify({"response": f"Post Request Called. Name: {name}"})
 
if __name__ == '__main__':
    app.run(debug=True, port=9090)