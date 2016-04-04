from flask_socketio import SocketIO, emit
from PiPocketGeiger import RadiationWatch
from web_portal import app
import time
try:
    import queue
except ImportError:
    import Queue as queue
import eventlet

radiationWatch = RadiationWatch(24, 23).setup()
# We need to close properly this resource at the appplication tear down.

socketio = SocketIO(app)
q = queue.Queue()

@socketio.on('connect')
def onConnect():
    print('Client connected')
    emit('readings', {
        'cpm': None,
        'uSvh': None,
        'uSvhError': None
        }, json=True)
    # TODO Send Historical data.
    # emit('historical', data, json=True)

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
            # TODO Send current readings.
            socketio.emit('readings',
                radiationWatch.status(),
                json=True)
        except queue.Empty:
            eventlet.sleep(0.1)

eventlet.spawn_n(listenToQueue)
radiationWatch.registerRadiationCallback(onRadiation)
