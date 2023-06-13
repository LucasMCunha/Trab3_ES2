from flask import Flask, request, jsonify

app = Flask(__name__)

import mysql.connector

def inserir_dados(codigo, name, horario, turma):
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='dbDisciplinas',
        user='root',
        password='root',
        database='disciplinas'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO Disciplinas (CodigoDisciplina, NomeDisciplina, HorarioDisciplina, Turma) VALUES ({}, {}, {}, {})"

    dados = (codigo, name, horario, turma)
    lista = sql.format(*dados)
    cursor.execute(lista)

    conexao.commit()

    cursor.close()
    conexao.close()


#5. Cadastrar disciplinas, com os dados: código da disciplina, nome da disciplina, horário da 
#disciplina (por códigos: A, B, C, D, E, F, G), turma da disciplina (código numérico). Lembre-se 
#que uma mesma disciplina (mesmo código e nome) pode ocorrer mais de uma vez (turmas 
#diferentes). 
@app.route('/disc', methods=['POST'])
def Register ():
    if request.method == "POST":
        req = request.args
        codigo = int(req['codigo'])
        name = req['name']
        name = "\""+name+"\""
        horario = req['horario']
        horario = "\""+horario+"\""
        turma = int(req['turma'])
        inserir_dados(codigo, name, horario, turma)
        return jsonify({"response": f"Disciplina nova criada. Codigo {codigo}, Name: {name}, Horario {horario}, Turma {turma}"})
 
if __name__ == '__main__':
    app.run(debug=True)