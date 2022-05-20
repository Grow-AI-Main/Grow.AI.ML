from flask import Flask, jsonify, request
from numpy import number

app = Flask(__name__)

@app.route('/ping/', methods=['GET', 'POST'])
def welcome():
    return "pong!"

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))

@app.route("/json", methods=["POST"])
def json_example():

    req = request.get_json()

    print(req)

    req['number'] += 5

    return jsonify(req), 201

if __name__ == '__main__':
    app.run(port=105)