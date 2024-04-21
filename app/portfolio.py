from flask import (
    Blueprint, render_template, request, redirect, url_for, current_app
)
import requests

bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route('/mail', methods=['GET', 'POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    if request.method == 'POST':
        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html')
    
    return redirect(url_for('portfolio.index'))

def send_email(name, email, message):
    try:
        my_email = 'kevinsteven.07.sg@gmail.com'        
        response = requests.post(
            f"https://api.mailgun.net/v3/{current_app.config['MAILGUN_DOMAIN']}/messages",
            auth=("api", current_app.config['MAILGUN_KEY']),
            data={"from": f"no-reply@{current_app.config['MAILGUN_DOMAIN']}",
                  "to": [my_email],
                  "subject": 'Contacto de cliente nuevo!',
                  "text": message + " from:" + email + " and his name is:" + name})
        if response.status_code != 200:
            print(f"Failed to send email: {response.text}")
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")