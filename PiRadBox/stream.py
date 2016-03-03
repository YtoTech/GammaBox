from flask_socketio import SocketIO, emit
from PiPocketGeiger import RadiationWatch
from web_portal import app
import time

radiationWatch = RadiationWatch(24, 23).setup()
# We need to close properly this resource at the appplication tear down.

socketio = SocketIO(app)

@socketio.on('connect')
def onConnect():
    print('Client connected')
    emit('readings', {
        'cpm': '-',
        'uSvh': '-'
        }, json=True)
    socketio.emit('ray', 'Hit!')
    # TODO Send Historical data.
    # emit('historical', data, json=True)

def onRadiation():
    # TODO Get back to our main eventlet thread.
    print("Ray hit")
    socketio.emit('ray', 'Hit!')
    socketio.send('Hit')
    # TODO Send current readings.
    # socketio.emit('ray', readings, json=True)

radiationWatch.registerRadiationCallback(onRadiation)
