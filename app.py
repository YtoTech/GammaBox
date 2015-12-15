from PiRadBox import socketio, app
import sys

if __name__ == "__main__":
    if '-d' in sys.argv or '--debug' in sys.argv:
        socketio.debug = True
    socketio.run(app, port=80, host='0.0.0.0')
