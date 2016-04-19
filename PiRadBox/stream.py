from flask_socketio import SocketIO, emit
from PiPocketGeiger import RadiationWatch
from web_portal import app
import time
try:
    import queue
except ImportError:
    import Queue as queue
import eventlet
import datetime

HISTORY_LENGTH = 500
radiationWatch = RadiationWatch(24, 23).setup()
# We need to close properly this resource at the appplication tear down.

socketio = SocketIO(app)
q = queue.Queue()
history = []

@socketio.on('connect')
def onConnect():
    # TODO Get current readings.
    print('Client connected')
    if history:
        emit('readings', {
            'timestamp': history[-1]['timestamp'],
            'cpm': history[-1]['cpm'],
            'uSvh': history[-1]['uSvh'],
            'uSvhError': history[-1]['uSvhError']
            }, json=True)
    else:
        emit('readings', {
            'cpm': None,
            'uSvh': None,
            'uSvhError': None
            }, json=True)
    # Send historical data.
    emit('history', history, json=True)

def onRadiation():
    # Get back to our main eventlet thread using a Queue
    # to transfer the signal from the interrupt thread
    # to the main thread.
    # TODO Or use a Python socketio client to communicate with this server.
    q.put_nowait(None)

def listenToQueue():
    while 1:
        try:
            data = q.get_nowait()
            socketio.emit('ray', data)
            print('Ray')
            readings = radiationWatch.status()
            readings['timestamp'] = datetime.datetime.now().isoformat() + 'Z'
            # Send current readings.
            socketio.emit('readings',
                readings,
                json=True)
            # Persist historical data.
            history.append(readings)
            while len(history) > HISTORY_LENGTH:
                del history[0]
        except queue.Empty:
            eventlet.sleep(0.1)

eventlet.spawn_n(listenToQueue)
radiationWatch.registerRadiationCallback(onRadiation)
