from flask import Flask, request, jsonify

app = Flask(__name__)

import mysql.connector

def inserir_dados(dados):
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        password='root',
        database='alunos_disciplinas'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO tabela (Matricula, CodigoDisciplina) VALUES (%d, %d)"

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()
    
def obter_dados():
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        password='root',
        database='alunos_disciplinas'
    )

    cursor = conexao.cursor()

    # Instrução SQL para selecionar os dados
    sql = "SELECT Matricula, CodigoDisciplina FROM Matriculas"

    # Executar a consulta SQL
    cursor.execute(sql)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Fechar conexão e cursor
    cursor.close()
    conexao.close()

    # Retornar os resultados
    return resultados

@app.route('/matdisc', methods=['POST'])
def Register ():
    req = request.args
    mat = req['matricula']
    codigo = req['codigo']
    inserir_dados(mat, codigo)
    return jsonify({"response": f"Aluno cadastrado na disciplina. Matricula: {mat}, Codigo: {codigo}"})

@app.route('/matdiscDisciplina', methods=['GET'])
def getDiscAluno():
    req = request.args
    mat = req['matricula']
    resposta = f"Aluno de matricula {mat}, cadastrado em disciplinas:"
    for d in obter_dados():
        if mat == d[0]:
            resposta += f"\n{d[1]}"
    return jsonify({"response": resposta})

@app.route('/matdiscAluno', methods=['GET'])
def getAlunosDisc():
    req = request.args
    codigo = req['codigo']
    resposta = f"Aluno de codigo {codigo}, com os alunos de matricula:"
    for d in obter_dados():
        if codigo == d[1]:
            resposta += f"\n{d[0]}"
    return jsonify({"response": resposta})

    
@app.route('/ola', methods=['GET'])
def ola():
    return "Ola reg mat disc"
    
if __name__ == '__main__':
    app.run(debug=True)