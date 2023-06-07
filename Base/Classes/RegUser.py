from flask import Flask, request, jsonify

app = Flask(__name__)

class User ():
    def __init__(self,nome: str,email: str,senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha


@app.route('/User', methods=['POST'])
def Register ():
    if request.method == "POST":
        req = request.args
        name = req['name']
        email = req['email']
        senha = req['senha']
        a = User(name, email, senha)
        #colocar no BD
        return jsonify({"response": f"Post Request Called. Name: {name}, Email: {email}"})
    
if __name__ == '__main__':
    app.run(debug=True, port=9090)