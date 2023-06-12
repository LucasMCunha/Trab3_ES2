from flask import Flask, request, jsonify

app = Flask(__name__)

import mysql.connector

def obter_dados():
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        password='root',
        database='users'
    )

    cursor = conexao.cursor()

    # Instrução SQL para selecionar os dados
    sql = "SELECT Email, Senha FROM Usuarios"

    # Executar a consulta SQL
    cursor.execute(sql)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Fechar conexão e cursor
    cursor.close()
    conexao.close()

    # Retornar os resultados
    return resultados

@app.route('/user', methods=['GET'])
def aluno():
    req = request.args
    email = req['email']
    senha = req['senha']
    for d in obter_dados():
        if email == d[0] and senha == d[1]:
            return jsonify({"response": "Usuario encontrado"})
    return jsonify({"response": "Usuario não encontrado"})
    
@app.route('/ola', methods=['GET'])
def ola():
    return "ola"

if __name__ == '__main__':
    app.run(debug=True)