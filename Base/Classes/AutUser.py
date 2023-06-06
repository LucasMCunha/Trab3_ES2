from flask import Flask, request, jsonify

app = Flask(__name__)

#def ...

@app.route('/user', methods=['GET'])
def aluno():
    if request.method == "GET": 
        return jsonify({"response": "User"})

if __name__ == '__main__':
    app.run(debug=True, port=9090)