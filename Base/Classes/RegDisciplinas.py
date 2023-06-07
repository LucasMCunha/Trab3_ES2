from flask import Flask, request, jsonify

app = Flask(__name__)

class Disciplina ():
    def __init__(self, codigo: int,nome: str,horario: str,turma: int):
        self.codigo = codigo
        self.nome = nome
        self.horario = horario
        self.turma = turma

    
@app.route('/disc', methods=['POST'])
def Register ():
    if request.method == "POST":
        req = request.args
        codigo = req['codigo']
        name = req['name']
        horario = req['horario']
        turma = req['turma']
        a = Disciplina(codigo, name, horario, turma)
        #colocar no BD
        return jsonify({"response": f"Post Request Called. Codigo {codigo}, Name: {name}, Horario {horario}, Turma {turma}"})
 
if __name__ == '__main__':
    app.run(debug=True, port=9090)