from flask import render_template
from datetime import datetime
from . import app

@app.route('/')
def index():
    return render_template('index.html', year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html', year=datetime.now().year)

@app.route('/quarterbacks')
def quarterbacks():
    return render_template('quarterbacks.html', year=datetime.now().year)
