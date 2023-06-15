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

def verifica_matricula(mat):
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='dbAlunos',
        user='root',
        password='root',
        database='alunos'
    )

    cursor = conexao.cursor()

    # Instrução SQL para selecionar os dados
    sql = "SELECT Matricula FROM Alunos"

    # Executar a consulta SQL
    cursor.execute(sql)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Fechar conexão e cursor
    cursor.close()
    conexao.close()
    
    for r in resultados:
        if r[0] == mat:
            return True
    return False

def verifica_disciplina(codigo, turma):
    conexao = mysql.connector.connect(
        host='dbDisciplinas',
        user='root',
        password='root',
        database='disciplinas'
    )
    
    cursor = conexao.cursor()

    # Instrução SQL para selecionar os dados
    sql = "SELECT CodigoDisciplina, Turma FROM Disciplinas"

    # Executar a consulta SQL
    cursor.execute(sql)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Fechar conexão e cursor
    cursor.close()
    conexao.close()
    
    for r in resultados:
        if r[0] == codigo and r[1] == turma:
            return True
    return False

#6. Matricular estudante em uma disciplina: informar número de matrícula do estudante, código 
#e turma da disciplina.
@app.route('/matdisc', methods=['POST'])
def Register ():
    req = request.args
    mat = int(req['matricula'])
    codigo = int(req['codigo'])
    turma = int(req['turma'])
    
    if not verifica_matricula(mat):
        return jsonify({"response": f"Aluno com a matricula {mat} não foi encontrado"})
    
    if not verifica_disciplina(codigo, turma):
        return jsonify({"response": f"Disciplina com a código {codigo} e turma {turma} não foi encontrado"})
    
    inserir_dados(mat, codigo, turma)
    return jsonify({"response": f"Aluno cadastrado na disciplina. Matricula: {mat}, Disciplina: {codigo}, Turma: {turma}"})

#7. Consultar as disciplinas/turmas em que um estudante está matriculado.
@app.route('/matdiscDisciplina', methods=['GET'])
def getDiscAluno():
    req = request.args
    mat = int(req['matricula'])
    if not verifica_matricula(mat):
        return jsonify({"response": f"Aluno com a matricula {mat} não foi encontrado"})
    resposta = f"Aluno de matricula {mat}, cadastrado em: "
    for d in obter_dados():
        if mat == d[0]:
            resposta += f" disciplina com código {d[1]} na turma número {d[2]}|"
    return jsonify({"response": resposta[:-1]})

#8. Consultar os estudantes matriculados em uma disciplina/turma.
@app.route('/matdiscAluno', methods=['GET'])
def getAlunosDisc():
    req = request.args
    codigo = int(req['codigo'])
    turma = int(req['turma'])
    if not verifica_disciplina(codigo, turma):
        return jsonify({"response": f"Disciplina com a código {codigo} e turma {turma} não foi encontrado"})
    resposta = f"Disciplina de codigo {codigo} na turma {turma}:"
    for d in obter_dados():
        if codigo == d[1] and turma == d[2]:
            resposta += f" aluno de matricula {d[0]};"
    return jsonify({"response": resposta[:-1]})
    
if __name__ == '__main__':
    app.run(debug=True)