import json
from flask import Flask, render_template, request, jsonify
from . import forward

# pylint: disable=C0103
app = Flask(__name__)
RADBOX_SETTINGS_FILE = "settings.json"
forwarder = forward.Forwarder(RADBOX_SETTINGS_FILE)

########################
# Front.               #
########################


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


########################
# API.               #
########################


@app.route("/api/settings", methods=["GET"])
def api_settings_get():
    with open(RADBOX_SETTINGS_FILE, "rb") as file:
        return jsonify(json.load(file))


@app.route("/api/settings", methods=["POST"])
def api_settings_post():
    with open(RADBOX_SETTINGS_FILE, "wb") as file:
        json.dump(request.get_json(), file)
    # TODO Use message passing.
    forwarder.reload_configuration()
    return "", 204
