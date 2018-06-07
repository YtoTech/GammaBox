"""
Launch the Gamma Box.
"""
import sys
import logging
import logging.handlers
from gammabox import socketio, app

# Configure logging.
# pylint: disable=C0103
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
# Rotate logging in a file.
rotatingFileHandler = logging.handlers.RotatingFileHandler(
    "log.txt", mode="a", maxBytes=500000, backupCount=3)
rootLogger.addHandler(logging.StreamHandler(sys.stdout))
rootLogger.addHandler(rotatingFileHandler)

if __name__ == "__main__":
    if "-d" in sys.argv or "--debug" in sys.argv:
        socketio.debug = True
    # TODO Make it configurable.
    socketio.run(app, port=8080, host="0.0.0.0")
