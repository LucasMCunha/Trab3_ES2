from flask import Flask, request, jsonify

app = Flask(__name__)

import mysql.connector

def inserir_dados(mat, codigo, turma):
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='dbAlunosDisciplinas',
        user='root',
        password='root',
        database='alunosDisciplinas'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO Matriculas (AlunoMatricula, DisciplinaCodigo, DisciplinaTurma) VALUES ({}, {}, {})"

    dados = (mat, codigo, turma)
    lista = sql.format(*dados)
    cursor.execute(lista)

    conexao.commit()

    cursor.close()
    conexao.close()
    
def obter_dados():
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='dbAlunosDisciplinas',
        user='root',
        password='root',
        database='alunosDisciplinas'
    )

    cursor = conexao.cursor()

    # Instrução SQL para selecionar os dados
    sql = "SELECT AlunoMatricula, DisciplinaCodigo, DisciplinaTurma FROM Matriculas"

    # Executar a consulta SQL
    cursor.execute(sql)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Fechar conexão e cursor
    cursor.close()
    conexao.close()

    # Retornar os resultados
    return resultados

id = 4 #O que é esse id?

#6. Matricular estudante em uma disciplina: informar número de matrícula do estudante, código 
#e turma da disciplina.
@app.route('/matdisc', methods=['POST'])
def Register ():
    req = request.args
    mat = int(req['matricula'])
    codigo = int(req['codigo'])
    turma = int(req['turma'])
    inserir_dados(mat, codigo, turma)
    return jsonify({"response": f"Aluno cadastrado na disciplina. Matricula: {mat}, Codigo: {codigo}"})

#7. Consultar as disciplinas/turmas em que um estudante está matriculado.
@app.route('/matdiscDisciplina', methods=['GET'])
def getDiscAluno():
    req = request.args
    mat = req['matricula']
    resposta = f"Aluno de matricula {mat}, cadastrado em disciplinas:"
    for d in obter_dados():
        if mat == d[0]:
            resposta += f"\n{d[1]}"
    return jsonify({"response": resposta})

#8. Consultar os estudantes matriculados em uma disciplina/turma.
@app.route('/matdiscAluno', methods=['GET'])
def getAlunosDisc():
    req = request.args
    codigo = req['codigo']
    resposta = f"Aluno de codigo {codigo}, com os alunos de matricula:"
    for d in obter_dados():
        if codigo == d[1]:
            resposta += f"\n{d[0]}"
    return jsonify({"response": resposta})
    
if __name__ == '__main__':
    app.run(debug=True)