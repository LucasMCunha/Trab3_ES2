from flask import Flask, request, jsonify

app = Flask(__name__)

class User ():
    def __init__(self,nome: str,email: str,senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha


def Register (nome: str, email: str, senha: str):
    a = User(nome, email, senha)
    #colocar no BD

@app.route('/User', methods=['POST'])
def user():
    if request.method == "POST":
        req = request.args
        name = req['name']
        return jsonify({"response": f"Post Request Called. Name: {name}"})
    
if __name__ == '__main__':
    app.run(debug=True, port=9090)