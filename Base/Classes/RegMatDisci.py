from flask import Flask, request, jsonify

import RegDisciplinas
import ConsAlunos
import RegAlunos

app = Flask(__name__)

class MatriculaDisciplina ():
    def __init__(self, aluno: RegAlunos.Aluno, disciplinas):
        self.aluno = aluno
        self.disciplinas = disciplinas

@app.route('/matdisc', methods=['POST'])
def Register ():
    req = request.args
    nameA = req['name aluno']
    mat = req['matricula']
    req = request.args
    codigo = req['codigo']
    nameD = req['name disciplina']
    horario = req['horario']
    turma = req['turma']
    return jsonify({"response": f"Post Request Called. Name: {nameA}"})

    a = MatriculaDisciplina(aluno, disciplinas)
    #colocar no BD
    
def getDiscAluno(aluno: RegAlunos.Aluno):
    if ConsAlunos.buscaAluno(aluno) != None:
        #pegar lista de disciplinas do banco a partir do nome do aluno
        for d in RegDisciplinas:
            print(d)

def getAlunosDisc(disciplina: RegDisciplinas.Disciplina):
    #pegar na base de dados todos os alunos
    for a in RegAlunos:
        print(a)


@app.route('/matdisc', methods=['GET', 'POST'])
def matDisc():
    if request.method == "GET": 
        return jsonify({"response": "MatDisc"})
    
    elif request.method == "POST":
        req = request.args
        name = req['name']
        return jsonify({"response": f"Post Request Called. Name: {name}"})
    
if __name__ == '__main__':
    app.run(debug=True, port=9090)