from flask import render_template
from app import app
from app.mailer import Mailer
from .date import calculate_year_from_current_date


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',
                           age=calculate_year_from_current_date(1999, 5, 25),
                           programming_since=calculate_year_from_current_date(2018, 3, 14))


@app.route('/contact')
def send_mail():
    Mailer().send()
