from flask_socketio import SocketIO, emit
from web_portal import app
import time

socketio = SocketIO(app)

@socketio.on('connect')
def onConnect():
    print('Client connected')
    emit('readings', {
        'cpm': '-',
        'uSvh': '-'
        }, json=True)
    # TODO Send Historical data.
    # emit('historical', data, json=True)

def onRadiation():
    print("Ray hit")
    socketio.emit('ray', 'Hit!')
    # TODO Send current readings.
    # socketio.emit('ray', readings, json=True)
