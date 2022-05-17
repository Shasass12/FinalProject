import random
import string

from flask import Flask

from pages.home.home import home
from pages.recommendation.recommendation import recommendation
from pages.sheelon.sheelon import sheelon
from pages.sheelon2.sheelon2 import sheelon2
from pages.sheelon3.sheelon3 import sheelon3
from pages.start.start import start
from pages.thankyou.thankyou import thankyou

app = Flask(__name__)
app.register_blueprint(sheelon)
app.register_blueprint(start)
app.register_blueprint(sheelon2)
app.register_blueprint(sheelon3)
app.register_blueprint(home)
app.register_blueprint(recommendation)
app.register_blueprint(thankyou)

secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
app.secret_key = secret_key

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, threaded=True)
