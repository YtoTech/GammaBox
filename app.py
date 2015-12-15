from PiRadBox import app
import sys

if __name__ == "__main__":
    if '-d' in sys.argv or '--debug' in sys.argv:
        app.debug = True
    app.run(port=80, host='0.0.0.0', threaded=True)
