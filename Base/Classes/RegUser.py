from flask import Flask, request, jsonify

app = Flask(__name__)

import mysql.connector

def inserir_dados(nome, email,senha):
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='dbUsers',
        user='root',
        password='root',
        database='users'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO Usuarios (Nome, Email, Senha) VALUES ({}, {}, {})"

    dados = (nome, email, senha)
    lista = sql.format(*dados)
    cursor.execute(lista)

    conexao.commit()

    cursor.close()
    conexao.close()

# 9. Registrar usuário do sistema, com seu e-mail, nome e senha para fins de 
# autenticação/autorização (ponto extra).
@app.route('/User', methods=['POST'])
def Register ():
    if request.method == "POST":
        req = request.args
        name = req['name']
        name = "\""+name+"\""
        email = req['email']
        email = "\""+email+"\""
        senha = req['senha']
        senha = "\""+senha+"\""
        inserir_dados(name, email, senha)
        
        return jsonify({"response": f"Usuário {name} com email: {email} cadastrado com sucesso!"})
    
if __name__ == '__main__':
    app.run(debug=True)