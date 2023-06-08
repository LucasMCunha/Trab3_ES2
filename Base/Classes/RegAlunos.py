from flask import Flask, request, jsonify

app = Flask(__name__)
matricula = 0

class Aluno ():
    def __init__(self,nome: str,numeroDoc: int,endereco: str,matricula: int):
        self.nome = nome
        self.numeroDoc = numeroDoc
        self.endereco = endereco
        self.matricula = matricula


@app.route('/aluno', methods=['POST'])
def Register ():
    global matricula
    matricula = matricula + 1
    if request.method == "POST":
        req = request.args
        name = req['name']
        numId= req['number ID']
        add = req['address']
        
        a = Aluno(name, numId, add, matricula)
        #colocar no BD
        return jsonify({"response": f"Post Request Called. Name: {name}, Number of ID: {numId}, Address: {add}, Matricula: {matricula}"})
 
if __name__ == '__main__':
    app.run(debug=True)