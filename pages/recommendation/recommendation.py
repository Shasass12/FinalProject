import random

from flask import Blueprint, render_template, request

recommendation = Blueprint('recommendation', __name__, static_folder='static', static_url_path='/recommendation',
                           template_folder='templates')
restaurant_title = ['המסעדה המתאימה ביותר עבורך היא', 'המסעדה הפופולארית ביותר במערכת היא',
                    'המסעדה האהובה על משתמשים דומים לך היא']


@recommendation.route('/recommendation')
def index():
    title = random.choice(restaurant_title)
    return render_template('recommendation.html', title=title, image=request.args['favourite_food_style'])
