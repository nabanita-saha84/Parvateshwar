import flask
from flask import render_template
from src import app

@app.route("/")
@app.route("/home/")
def home():
	return render_template("home.html")