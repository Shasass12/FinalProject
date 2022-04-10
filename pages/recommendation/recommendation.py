import random

from flask import Blueprint, render_template, request

recommendation = Blueprint('recommendation', __name__, static_folder='static', static_url_path='/recommendation',
                           template_folder='templates')
restaurant_title = ['לפי התאמה אישית, המלצת המערכת היא', 'לפי פופולריות, המלצת המערכת היא',
                    'לפי משתמשים הדומים לך, המלצת המערכת היא']


@recommendation.route('/recommendation')
def index():
    title = random.choice(restaurant_title)
    return render_template('recommendation.html', title=title, image=request.args['favourite_food_style'])
