import logics
import data_frame_manager
from flask import Flask, jsonify, request


logics = logics.Logics()
data_frame_manager = data_frame_manager.DataFrameManager()

app = Flask(__name__)


@app.route('/ping', methods=['GET', 'POST'])
def welcome():
    return "pong!"


@app.route("/analyze", methods=["POST"])
def analyze():
    req = request.get_json()

    analyzed_user_data = logics.analyze_user(req)

    return jsonify(analyzed_user_data), 200


@app.route("/resources/titles", methods=['GET'])
def titles():
    titles = data_frame_manager.get_unique_titles()

    return jsonify(titles=titles)


@app.route("/resources/degree/types", methods=['GET'])
def degree_types():
    degree_types = data_frame_manager.get_unique_degree_types()

    return jsonify(types=degree_types)


@app.route("/resources/degree/fields", methods=['GET'])
def degree_fields():
    degree_fields = data_frame_manager.get_unique_degree_fields()

    return jsonify(fields=degree_fields)


@app.route("/resources/degree/institutions", methods=['GET'])
def degree_institutions():
    degree_institutions = data_frame_manager.get_unique_degree_institutions()

    return jsonify(institutions=degree_institutions)


if __name__ == '__main__':
    app.run(port=105)