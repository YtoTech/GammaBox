debug:
	python app.py --debug

run:
	gunicorn --bind 0.0.0.0:80 app:app
