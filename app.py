import flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run()
