from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
app.secret_key = 'sjdfhaklehfliuehflkajsdhflkajdhflkjabdsvlakbsdvklahfoawhef'
socketio = SocketIO(app)


app.config['SESSION_TYPE'] = 'filesystem'


from app.routes import app


