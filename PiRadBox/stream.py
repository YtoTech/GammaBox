from flask_socketio import SocketIO, emit
from PiPocketGeiger import RadiationWatch
from web_portal import app
import time
try:
    import queue
except ImportError:
    import Queue as queue
import eventlet
eventlet.monkey_patch()

radiationWatch = RadiationWatch(24, 23).setup()
# We need to close properly this resource at the appplication tear down.

socketio = SocketIO(app)
q = queue.Queue()

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
    # TODO Get back to our main eventlet thread: how to to that?
    # Use a Queue, then create a greenlet that poll to the queue?
    # Or use a Python socketio client to communicate with this server.
    print("Ray hit")
    q.put('Hit!')
    # socketio.emit('ray', 'Hit!')
    # TODO Send current readings.
    # socketio.emit('ray', readings, json=True)

def listenToQueue():
    while 1:
        # This is fucking ugly! We're polling as hell.
        try:
            data = q.get(block=False)
            print(data)
            socketio.emit('ray', data)
        except queue.Empty:
            eventlet.sleep(0.1)

eventlet.spawn(listenToQueue)

radiationWatch.registerRadiationCallback(onRadiation)

