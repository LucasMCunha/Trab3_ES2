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
    return jsonify({"response": f"Aluno cadastrado na disciplina. Matricula: {mat}, Disciplina: {codigo}, Turma: {turma}"})

#7. Consultar as disciplinas/turmas em que um estudante está matriculado.
@app.route('/matdiscDisciplina', methods=['GET'])
def getDiscAluno():
    req = request.args
    mat = int(req['matricula'])
    resposta = f"Aluno de matricula {mat}, cadastrado em: "
    for d in obter_dados():
        if mat == d[0]:
            resposta += f"disciplina com código {d[1]}/turma número {d[2]}|"
    return jsonify({"response": resposta[:-1]})

#8. Consultar os estudantes matriculados em uma disciplina/turma.
@app.route('/matdiscAluno', methods=['GET'])
def getAlunosDisc():
    req = request.args
    codigo = int(req['codigo'])
    turma = int(req['turma'])
    resposta = f"Disciplinas de codigo {codigo} na turma {turma}:"
    for d in obter_dados():
        if codigo == d[1] and turma == d[2]:
            resposta += f"Alunos de matricula {d[0]};"
    return jsonify({"response": resposta[:-1]})
    
if __name__ == '__main__':
    app.run(debug=True)