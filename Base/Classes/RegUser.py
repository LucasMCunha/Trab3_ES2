from flask import Flask, request, jsonify

app = Flask(__name__)

import mysql.connector

def inserir_dados(id, nome, email,senha):
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='dbUsers',
        user='root',
        password='root',
        database='users'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO Usuarios (ID, Nome, Email, Senha) VALUES ({}, {}, {}, {})"

    dados = (id, nome, email, senha)
    lista = sql.format(*dados)
    cursor.execute(lista)

    conexao.commit()

    cursor.close()
    conexao.close()

id = 1

@app.route('/User', methods=['POST'])
def Register ():
    global id
    if request.method == "POST":
        req = request.args
        name = req['name']
        name = "\""+name+"\""
        email = req['email']
        email = "\""+email+"\""
        senha = req['senha']
        senha = "\""+senha+"\""
        inserir_dados(id, name, email, senha)
        id = id + 1
        
        return jsonify({"response": f"Usuário {name} com email: {email} cadastrado com sucesso!"})
    
if __name__ == '__main__':
    app.run(debug=True)