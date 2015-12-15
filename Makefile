debug:
	python app.py --debug

run:
	gunicorn --worker-class eventlet --bind 0.0.0.0:80 app:app
