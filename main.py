from source import google
from flask import Flask

app = Flask(__name__)

@app.route('/extract')
def extract():
    return google.extract()
