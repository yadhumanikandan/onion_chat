from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'sjdfhaklehfliuehflkajsdhflkajdhflkjabdsvlakbsdvklahfoawhef'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SESSION_TYPE'] = 'filesystem'


db = SQLAlchemy(app)

#import tables
from app.models import users


from app.routes import app


with app.app_context():
    db.create_all()

