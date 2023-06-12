from flask import Flask, request, jsonify

app = Flask(__name__)

import mysql.connector

def inserir_dados(dados):
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        password='root',
        database='users'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO tabela (ID, Nome, Email, Senha) VALUES (%d, %s, %s, %s)"

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

id = 0

@app.route('/User', methods=['POST'])
def Register ():
    if request.method == "POST":
        req = request.args
        name = req['name']
        email = req['email']
        senha = req['senha']
        a = inserir_dados(id, name, email, senha)
        id = id + 1
        
        return jsonify({"response": f"Usuário {name} com email: {email} cadastrado com sucesso!"})
    
@app.route('/ola', methods=['GET'])
def ola():
    return "Ola reg user"
    
if __name__ == '__main__':
    app.run(debug=True)