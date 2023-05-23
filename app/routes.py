from flask import render_template, session, redirect, url_for, request
from app import app




@app.route("/")
def index():
    return render_template('home.html')
    #check if user already in session
    # if "email" in session:
    #     return redirect(url_for("home"))
    # else:
    #     return redirect(url_for("login"))