import os

from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/<route>')
def send_static_route(route):
    return send_from_directory('static', route)


if __name__ == '__main__':
    app.run(host=os.environ.get('HOST', '0.0.0.0'), port=int(os.environ.get('PORT')))
