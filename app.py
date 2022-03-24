import flask
from flask import Flask
from pages.home.home import home
from pages.sheelon.sheelon import sheelon

from pages.sheelon2.sheelon2 import sheelon2
from pages.recommendation.recommendation import recommendation

app = Flask(__name__)
app.register_blueprint(sheelon)
app.register_blueprint(sheelon2)
app.register_blueprint(home)
app.register_blueprint(recommendation)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, threaded=True)
