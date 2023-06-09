from flask import Flask, request, jsonify

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
    return "funcionou"

@app.route('/alunos/nome', methods=['GET'])
def buscaNome ():
    req = request.args
    parte = req['name']
    for aluno in alunos:
        for i in range(len(aluno['name']) - len(parte)):
            if parte == aluno['name'][i:i + len(parte)]:
                print(aluno)
                return jsonify(aluno)  # Retornar o aluno como uma resposta JSON

@app.route('/alunos/matricula', methods=['GET'])
def buscaMatricula ():
    req = request.args
    mat = req['matricula']
    for aluno in alunos:
        if mat == aluno['matricula']:
            print(aluno)
            return jsonify(aluno)  # Retornar o aluno como uma resposta JSON

@app.route('/alunos/aluno', methods=['GET'])
def buscaAluno():
    req = request.args
    name = req['name']
    numId = req['number ID']
    add = req['address']
    mat = req['matricula']
    # Adicione a lógica de busca aqui
    for aluno in alunos:
        if name == aluno['name'] and numId == aluno['number ID']:
            return jsonify(aluno)  # Retornar o aluno como uma resposta JSON
    return "Aluno não encontrado"

if __name__ == '__main__':
    app.run(debug=True)