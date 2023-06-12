from flask import Flask, request, jsonify

app = Flask(__name__)

#def ...

@app.route('/user', methods=['GET'])
def aluno():
    if request.method == "GET": 
        return jsonify({"response": "User"})
    
@app.route('/ola', methods=['GET'])
def ola():
    return "ola"

if __name__ == '__main__':
    app.run(debug=True)