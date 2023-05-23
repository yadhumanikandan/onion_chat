from flask import render_template, session, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.models import users




@app.route("/")
def index():
    # check if user already in session
    if "email" in session:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))
    

@app.route("/login", methods=["POST", "GET"])
def login():
    if "username" in session:
        return redirect(url_for("home"))
    else:
        if request.method == "POST":
            found_user = users.query.filter_by(username=request.form["username"]).first()
            if found_user == None: 
                return redirect(url_for("signup"))
            elif check_password_hash(found_user.password_hash, request.form["password"]):
                # session["email"] = request.form["email"]
                session["username"] = found_user.username
                # session.permanent = True
                return redirect(url_for("home"))
            else:
                return redirect(url_for("login"))
            
        else:
            return render_template("login.html")
        

@app.route("/home")
def home():
    #check if user alreasy logged in
    if "username" in session:
        return render_template("home.html", username = session["username"])
    else:
        return redirect(url_for("login"))
    


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        found_user = users.query.filter_by(username = request.form["username"]).first()
        #check if user already exist in database
        if found_user == None:
            #if user not exit
            session["username"] = request.form["username"]
            # session["email"] = request.form["email"]
            # session.permanent = True

            password_hash = generate_password_hash(request.form["password"])
            usr = users(session["username"], password_hash)
            db.session.add(usr)
            db.session.commit()
            return redirect(url_for("home"))
        else:
            #if already exist
            return "<h1>user already exist <a href='/login'>LOGIN HERE</a></h1>"
    else:
        return render_template("register.html")



@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
