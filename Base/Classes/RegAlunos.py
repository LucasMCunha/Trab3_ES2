from flask import Flask, request, jsonify

app = Flask(__name__)
matricula = 1

import mysql.connector

def inserir_dados(name, numId, add):
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='dbAlunos',
        user='root',
        password='root',
        database='alunos'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO Alunos (Nome, DocumentoIdentificacao, Endereco) VALUES ({}, {}, {})"
    dados = (name, numId, add)
    lista = sql.format(*dados)
    cursor.execute(lista)

    conexao.commit()

    cursor.close()
    conexao.close()

#1. Registrar um estudante: nome, número do documento de identificação, endereço. Ao 
#cadastrar um estudante (evitando duplicações) cria-se um número de matrícula para o 
#estudante.
@app.route('/aluno', methods=['POST'])
def Register ():
    #matricula = matricula + 1
    
    if request.method == "POST":
        req = request.args

        name = req['name']
        name = "\""+name+"\""

        numId= int(req['numberID'])

        add = req['address']
        add = "\"" + add + "\""

        inserir_dados(name, numId, add)

        return jsonify({"response": f"Novo aluno cadastrado. Name: {name}, Number of ID: {numId}, Address: {add}"})
 
if __name__ == '__main__':
    app.run(debug=True)
