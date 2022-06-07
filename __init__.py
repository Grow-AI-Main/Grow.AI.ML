import logics
import data_frame_manager
from flask import Flask, jsonify, request
from flask_cors import CORS


logics = logics.Logics()
data_frame_manager = data_frame_manager.DataFrameManager()

app = Flask(__name__)
CORS(app)


@app.route('/ping', methods=['GET', 'POST'])
def welcome():
    return "pong!"


@app.route('/analyze', methods=['POST'])
def analyze():
    req = request.get_json()

    analyzed_user_data = logics.analyze_user(req)

    return jsonify(analyzed_user_data), 200


@app.route('/resources/destination_jobs', methods=['GET'])
def destination_jobs():
    destination_jobs = data_frame_manager.get_unique_destination_jobs()

    return jsonify(destination_jobs=destination_jobs)


@app.route('/resources/titles', methods=['GET'])
def titles():
    titles = data_frame_manager.get_unique_titles()

    return jsonify(titles=titles)


@app.route('/resources/degree/types', methods=['GET'])
def degree_types():
    degree_types = data_frame_manager.get_unique_degree_types()

    return jsonify(types=degree_types)


@app.route('/resources/degree/fields', methods=['GET'])
def degree_fields():
    degree_fields = data_frame_manager.get_unique_degree_fields()

    return jsonify(fields=degree_fields)


@app.route('/resources/degree/institutions', methods=['GET'])
def degree_institutions():
    degree_institutions = data_frame_manager.get_unique_degree_institutions()

    return jsonify(institutions=degree_institutions)


@app.route('/resources/degree/filter/<string:degree_type>', methods=['GET'])
def filter_degree_types(degree_type):
    degree_fields = data_frame_manager.get_unique_degree_fields_by_degree_type(degree_type)

    return jsonify(fields=degree_fields)


@app.route('/resources/degree/filter/<string:degree_type>/<string:degree_field>', methods=['GET'])
def filter_degree_institutions(degree_type, degree_field):
    degree_institutions = data_frame_manager.get_unique_degree_institutions_by_degree_type_and_degree_field(degree_type, degree_field)

    return jsonify(institutions=degree_institutions)


@app.errorhandler(ValueError)
def value_error(e):          
    return f'A value error occurred: {e}', 404


@app.errorhandler(Exception)
def basic_error(e):      
    return f'An exception occurred: {e}', 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)