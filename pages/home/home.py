from flask import Blueprint, render_template, request, redirect, url_for, session
from interact_with_db import get_keys

home = Blueprint('home', __name__, static_folder='static', static_url_path='/home', template_folder='templates')


@home.route('/')
def index():
    return render_template('home.html')


@home.route('/home_validate', methods=['POST'])
def validate_key_and_start():
    given_key = request.form['code']
    user_agent = request.headers.get('User-Agent')
    keys = get_keys()
    keys.append(('TEST-DESKTOP', False, False))
    keys.append(('TEST-MOBILE', True, False))
    session['key'] = given_key
    error_msg = ''
    found_key = False
    for key in keys:
        if key[0] == given_key:
            found_key = True
            # Key was used if key[2] is True
            if key[2]:
                error_msg = 'המפתח כבר בשימוש'
            else:
                if is_mobile_device(user_agent):
                    # request from mobile, but key for desktop
                    if not key[1]:
                        error_msg = 'הקוד מתאים למחשב, לא לפלאפון, נא להתחבר מהמחשב'
                # If desktop and request was from desktop
                else:
                    # request from desktop
                    if key[1]:
                        # request from desktop but key for mobile
                        error_msg = 'הקוד מתאים לפלאפון, לא למחשב, נא להתחבר מהפלאפון'
    if not found_key:
        error_msg = 'הקוד לא נכון, אנא וודא שהכנסת נכון את הקוד'
    if error_msg:
        return render_template('home.html', error_msg=error_msg)
    return redirect(url_for('start.index'))


def is_mobile_device(user_agent):
    result = False
    devices = ["Android", "webOS", "iPhone", "iPad", "iPod", "BlackBerry", "IEMobile", "Opera Mini"]
    if any(device in user_agent for device in devices):
        result = True
    return result
