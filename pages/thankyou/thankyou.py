from flask import Blueprint, render_template, request, redirect, url_for, session



thankyou = Blueprint('thankyou', __name__, static_folder='static', static_url_path='/thankyou',
                     template_folder='templates')


@thankyou.route('/thankyou')
def index():
    return render_template('thankyou.html')
