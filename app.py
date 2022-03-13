import flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return flask.render_template('index.html')

#@app.route('/goSomeWhere')
#def some_name():  # put application's code here
#    return flask.render_template('other_class.html')



if __name__ == '__main__':
    app.run()
