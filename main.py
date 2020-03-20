from source import google
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/extract', methods=['GET'])
def extract():
    if (request.method == 'GET'):
        return jsonify(google.extract())
    else:
        request jsonify({'message': 'Wrong request method'})
