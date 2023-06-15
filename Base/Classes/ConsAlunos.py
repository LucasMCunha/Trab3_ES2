from flask import Flask, request, jsonify

app = Flask(__name__)

import mysql.connector

def obter_dados():
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='dbAlunos',
        user='root',
        password='root',
        database='alunos'
    )

    cursor = conexao.cursor()

    # Instrução SQL para selecionar os dados
    sql = "SELECT Matricula, Nome, DocumentoIdentificacao, Endereco FROM Alunos"

    # Executar a consulta SQL
    cursor.execute(sql)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Fechar conexão e cursor
    cursor.close()
    conexao.close()

    # Retornar os resultados
    return resultados

#2. Consultar um estudante pelo número de matrícula. 
@app.route('/alunos/matricula', methods=['GET'])
def buscaMatricula ():
    req = request.args
    mat = int(req['matricula'])
    for aluno in obter_dados():
        if mat == aluno[0]:
            return jsonify(aluno)  # Retornar o aluno como uma resposta JSON
    return "Aluno não encontrado"

#3. Consultar um estudante por um pedaço de seu nome. Se houver mais de um "match", 
#retornar uma lista.
@app.route('/alunos/nome', methods=['GET'])
def buscaNome ():
    req = request.args
    parte = req['name']
    listaAlunos = []
    for aluno in obter_dados():
        if(aluno[1].find(parte) != -1):
            listaAlunos.append(aluno)
    return jsonify(listaAlunos)

# 4. Consultar a lista de todos os estudantes.
@app.route('/alunos/todos', methods=['GET'])
def buscaTodos (): 
    return jsonify(obter_dados())

if __name__ == '__main__':
    app.run(debug=True)
