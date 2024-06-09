import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

import models

@app.route('/')
def index():
    message = 'Hello, world!'
    print(f"Rendering index template with message: {message}")
    return render_template('ASQW.html', message=message)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Send an email or save the data to a database here
        return 'Thanks for your message!'
    return render_template('contact.html')
