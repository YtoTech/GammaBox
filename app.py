from PiRadBox import socketio, app
import sys
import logging
import logging.handlers

# Configure logging.
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
# We don't want a terminal handler as the process will be attached
# to the user terminal. (So if we have a terminal handler, flood happened)
rootLogger.removeHandler(rootLogger.handlers[0])
# Rotate logging in a file.
rotatingFileHandler = logging.handlers.RotatingFileHandler(
	'log.txt', mode='a', maxBytes=5000, backupCount=3)
rootLogger.addHandler(rotatingFileHandler)

if __name__ == "__main__":
    if '-d' in sys.argv or '--debug' in sys.argv:
        socketio.debug = True
    socketio.run(app, port=80, host='0.0.0.0')
