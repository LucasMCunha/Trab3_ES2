from flask import Flask, request, jsonify
import AutUser
import ConsAlunos
import RegAlunos
import RegDisciplinas
import RegMatDisci
import RegUser


app = Flask(__name__)

@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
    if request.method == "GET": 
        return jsonify({"response": "Aluno"})

    elif request.method == "POST":
        req = request.args
        name = req['name']
        numId= req['number ID']
        add = req['address']
        return jsonify({"response": f"Post Request Called. Name: {name}, Number of ID: {numId}, Address: {add}"})
    
#-----------------------------------------------------  

@app.route('/disc', methods=['GET', 'POST'])
def disciplina():
    if request.method == "GET": 
        return jsonify({"response": "Disciplina"})

    elif request.method == "POST":
        req = request.args
        name = req['name']
        return jsonify({"response": f"Post Request Called. Name: {name}"})
    
#-----------------------------------------------------

@app.route('/matdisc', methods=['GET', 'POST'])
def matDisc():
    if request.method == "GET": 
        return jsonify({"response": "MatDisc"})
    
    elif request.method == "POST":
        req = request.args
        name = req['name']
        return jsonify({"response": f"Post Request Called. Name: {name}"})
    
#-----------------------------------------------------

@app.route('/User', methods=['GET', 'POST'])
def user():
    if request.method == "GET": 
        return jsonify({"response": "User"})

    elif request.method == "POST":
        req = request.args
        name = req['name']
        return jsonify({"response": f"Post Request Called. Name: {name}"})
    
#-----------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=9090)