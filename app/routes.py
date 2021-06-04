from flask import render_template, request, flash

from app import app
from app.mailer import Mailer
from .date import calculate_year_from_current_date


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html',
                           age=calculate_year_from_current_date(1999, 5, 25),
                           programming_since=calculate_year_from_current_date(2018, 3, 14))


@app.route('/contact', methods=['POST'])
def send_mail():
    try:
        Mailer(sender_name=request.form['name'], sender_email=request.form['email'],
               subject=request.form['subject'], content=request.form['message']).send()
    except:
        flash('Oops something went wrong sending the message! Either try again or reach out yourself!', 'danger')
        return render_template('index.html')
    flash("Email has been send!", 'success')
    return render_template('index.html', succes='Email has been sent')
