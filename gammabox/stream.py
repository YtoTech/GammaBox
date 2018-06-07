"""Capture the Geiger counter readings and dispatch them
to the web app frontend and the forwarder.
Ideally we should have this in a separate program, so we can
reliably monitore the Geiger counter. This program would then
forward the readings using a broker (like ZeroMQ) to a backend
service (to store and forward the messages) and a frontend
service (to broadcast them). That way the reading part will
be less sensitive to issues from the backend or frontend processes.
"""
try:
    import queue
except ImportError:
    import Queue as queue
import logging
import datetime
import eventlet
from flask_socketio import SocketIO, emit
from PiPocketGeiger import RadiationWatch
from .web_portal import app, forwarder

HISTORY_LENGTH = 500
# pylint: disable=C0103
radiation_watch = RadiationWatch(24, 23).setup()
# We need to close properly this resource at the appplication tear down.

socketio = SocketIO(app)
gamma_queue = queue.Queue()
history = []


@socketio.on("connect")
def on_connect():
    # TODO Get current readings.
    logging.info("Client connected")
    if history:
        emit(
            "readings",
            {
                "timestamp": history[-1]["timestamp"],
                "cpm": history[-1]["cpm"],
                "uSvh": history[-1]["uSvh"],
                "uSvhError": history[-1]["uSvhError"],
            },
            json=True,
        )
    else:
        emit(
            "readings", {
                "cpm": None,
                "uSvh": None,
                "uSvhError": None
            },
            json=True)
    # Send historical data.
    emit("history", history, json=True)


def on_radiation():
    # Get back to our main eventlet thread using a Queue
    # to transfer the signal from the interrupt thread
    # to the main thread.
    # TODO Or use a Python socketio client to communicate with this server.
    gamma_queue.put_nowait(None)


def listen_to_queue():
    while 1:
        try:
            data = gamma_queue.get_nowait()
            socketio.emit("ray", data)
            readings = radiation_watch.status()
            readings["timestamp"] = datetime.datetime.now().isoformat() + "Z"
            # Send current readings.
            socketio.emit("readings", readings, json=True)
            # Persist historical data.
            history.append(readings)
            while len(history) > HISTORY_LENGTH:
                del history[0]
            # Dispatch readings.
            forwarder.dispatch(readings)
        except queue.Empty:
            eventlet.sleep(0.1)


eventlet.spawn_n(listen_to_queue)
radiation_watch.register_radiation_callback(on_radiation)
# TODO Also register noise an **dring** when noise present.
# (Show a message + some recommendation for noise prevention)
