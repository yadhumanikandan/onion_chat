from flask import Flask


app = Flask(__name__)
app.secret_key = 'sjdfhaklehfliuehflkajsdhflkajdhflkjabdsvlakbsdvklahfoawhef'


from app.routes import app

