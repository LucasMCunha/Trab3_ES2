from flask import Flask, request, jsonify

app = Flask(__name__)
matricula = 2

import mysql.connector

def retornaMatricula() -> int:
    with open('register.txt', 'r') as file:
        data = file.readlines()
        aux = int(data[0])
        data[0] = str(aux+1)
        with open('register.txt', 'w') as file:
            file.writelines(data)
        return aux

def inserir_dados(matricula, name, numId, add):
    matricula = retornaMatricula()
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='dbAlunos',
        user='root',
        password='root',
        database='alunos'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO Alunos (Matricula, Nome, DocumentoIdentificacao, Endereco) VALUES ({}, {}, {}, {})"
    dados = (matricula, name, numId, add)
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
    global matricula
    #matricula = matricula + 1
    
    if request.method == "POST":
        req = request.args

        name = req['name']
        name = "\""+name+"\""

        numId= int(req['numberID'])

        add = req['address']
        add = "\"" + add + "\""

        inserir_dados(matricula, name, numId, add)

        return jsonify({"response": f"Novo aluno cadastrado. Name: {name}, Number of ID: {numId}, Address: {add}, Matricula: {matricula}"})
 
if __name__ == '__main__':
    app.run(debug=True)
