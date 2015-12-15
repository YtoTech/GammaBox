from PiPocketGeiger import RadiationWatch
from stream import socketio

def onRadiation():
    print("Ray hit")
    socketio.send('Ray', namespace='/radiation/rays')
