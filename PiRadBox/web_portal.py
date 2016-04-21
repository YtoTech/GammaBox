from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
# TODO Persist and load settings to file.
# TODO Create an object accessible from the app methods.
radboxSettings = None

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')

# API.

@app.route("/api/settings", methods=['GET'])
def api_settings_get():
    print(radboxSettings)
    return jsonify(settings)

@app.route("/api/settings", methods=['POST'])
def api_settings_post():
    print(request.get_json())
    radboxSettings = request.get_json()
    return '', 204
