from flask import Flask, request, jsonify
import RegAlunos

app = Flask(__name__)

alunos = [
    {
        'name': 'João',
        'number ID': 123456789,
        'address': 'Rua 1',
        'matricula': 1
    },
    {
        'name': 'Maria',
        'number ID': 987654321,
        'address': 'Rua A',
        'matricula': 2 
    }
]

@app.route('/alunos/todos', methods=['GET'])
def buscaTodos (): 
    return jsonify(alunos)

@app.route('/alunos/nome', methods=['GET'])
def buscaNome ():
    req = request.args
    parte = req['name']
    for aluno in alunos:
        for i in range(len(aluno.nome)-len(parte)):
            if(parte == aluno.nome[i,len(parte)]):
                print(aluno)
                return aluno

@app.route('/alunos/matricula', methods=['GET'])
def buscaMatricula ():
    req = request.args
    mat = req['matricula']
    for aluno in alunos:
        if(mat == aluno.matricula):
            print(aluno)

@app.route('/alunos/aluno', methods=['GET'])           
def buscaAluno (aluno: RegAlunos.Aluno):
    req = request.args
    name = req['name']
    numId= req['number ID']
    add = req['address']
    mat = req['matricula']
    aluno = RegAlunos.Aluno(name, numId, add, mat)
    for a in alunos:
        if aluno.nome == a.nome and aluno.matricula == a.matricula: 
            return a
    
if __name__ == '__main__':
    app.run(debug=True)