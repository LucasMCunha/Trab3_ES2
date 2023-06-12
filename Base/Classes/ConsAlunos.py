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
    return alunos

@app.route('/alunos/nome', methods=['GET'])
def buscaNome ():
    req = request.args
    parte = req['name']
    for aluno in alunos:
        if parte == aluno['name']:            
            return jsonify(aluno)  # Retornar o aluno como uma resposta JSON
    return "Aluno não encontrado"

@app.route('/alunos/matricula', methods=['GET'])
def buscaMatricula ():
    req = request.args
    mat = int(req['matricula'])
    for aluno in alunos:
        if mat == aluno['matricula']:
            return jsonify(aluno)  # Retornar o aluno como uma resposta JSON
    return "Aluno não encontrado"

@app.route('/alunos/aluno', methods=['GET'])
def buscaAluno():
    req = request.args
    name = req['name']
    numId = int(req['number ID'])
    add = req['address']
    mat = int(req['matricula'])
    # Adicione a lógica de busca aqui
    for aluno in alunos:
        if name == aluno['name'] and numId == aluno['number ID'] and add == aluno['address'] and mat == aluno['matricula']:
            return jsonify(aluno)  # Retornar o aluno como uma resposta JSON
    return "Aluno não encontrado"

if __name__ == '__main__':
    print("TESTE")
    app.run(debug=True)