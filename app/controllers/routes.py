from datetime import datetime
from flask import Flask, url_for, render_template, redirect

from app import app

year = datetime.now().strftime('%Y')

@app.route('/')
async def index():
    return render_template("index.jinja2", year=year)

@app.route('/about')
async def about():
    return render_template("about.jinja2", year=year)

@app.get('/contact')
@app.post('/contact')
async def contact():
    return render_template('contact.jinja2', year=year)