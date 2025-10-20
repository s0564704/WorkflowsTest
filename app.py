from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Database connection with hardcoded credentials (NOT USED - for linter testing)
db_config = {
    'host': 'localhost',
    'database': 'mydb',
    'user': 'admin',
    'password': 'SuperSecret123!',
    'port': 5432
}

# Custom headers
@app.after_request
def add_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS, TRACE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Endpoint 1: Simple GET only
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello World!', 'status': 'success'})

# Endpoint 2: GET, POST, PUT, OPTIONS
@app.route('/api/data', methods=['GET', 'POST', 'PUT', 'OPTIONS'])
def data():
    if request.method == 'GET':
        return jsonify({'data': [1, 2, 3, 4, 5]})
    elif request.method == 'POST':
        return jsonify({'message': 'Data created', 'received': request.get_json()}), 201
    elif request.method == 'PUT':
        return jsonify({'message': 'Data updated', 'received': request.get_json()})
    elif request.method == 'OPTIONS':
        return '', 204

# Endpoint 3: GET, POST, PUT, TRACE, OPTIONS
@app.route('/api/info', methods=['GET', 'POST', 'PUT', 'TRACE', 'OPTIONS'])
def info():
    if request.method == 'GET':
        return jsonify({'info': 'System information', 'version': '1.0.0'})
    elif request.method == 'POST':
        return jsonify({'message': 'Info posted', 'data': request.get_json()}), 201
    elif request.method == 'PUT':
        return jsonify({'message': 'Info updated', 'data': request.get_json()})
    elif request.method == 'TRACE':
        return jsonify({'method': 'TRACE', 'path': request.path})
    elif request.method == 'OPTIONS':
        return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

