from flask_socketio import SocketIO, emit
from web_portal import app
import time

# Please read the doc: https://flask-socketio.readthedocs.org/en/latest/

socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('connect', namespace='/chat')
def test_connect():
    emit('my response', {'data': 'Connected'})

def onRadiation():
    print("Ray hit")
    socketio.send('Ray', namespace='/radiation/rays')
