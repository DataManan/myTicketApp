from flask import render_template

def homepage():

    return render_template("index.html.jinja2")