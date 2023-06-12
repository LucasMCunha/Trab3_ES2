from flask import Flask, request, jsonify

app = Flask(__name__)
matricula = 0

import mysql.connector

def inserir_dados(dados):
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        password='root',
        database='alunos'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO tabela (Matricula, Nome, DocumentoIdentificacao, Endereco) VALUES (%d, %s, %d, %s)"

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()


@app.route('/aluno', methods=['POST'])
def Register ():
    global matricula
    matricula = matricula + 1
    if request.method == "POST":
        req = request.args
        name = req['name']
        numId= req['number ID']
        add = req['address']
        inserir_dados(matricula, name, numId, add)
        return jsonify({"response": f"Novo aluno cadastrado. Name: {name}, Number of ID: {numId}, Address: {add}, Matricula: {matricula}"})
    
@app.route('/ola', methods=['GET'])
def ola():
    return "Ola"
 
if __name__ == '__main__':
    app.run(debug=True)