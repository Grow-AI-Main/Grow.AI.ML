import logics
from flask import Flask, jsonify, request

logics = logics.Logics()
app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST'])
def welcome():
    return "pong!"

@app.route("/analyze", methods=["POST"])
def analyze():

    req = request.get_json()

    analyzed_user_data = logics.analyze_user(req)

    return jsonify(analyzed_user_data), 200

if __name__ == '__main__':
    app.run(port=105)