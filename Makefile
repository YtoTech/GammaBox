################################################
#                 Installation                 #
################################################

install:
	pipenv install

################################################
#            Tests & Code analysis             #
################################################

test:
	pipenv run pytest

lint:
	pipenv run pylint .
	# TODO Add also flake8?

format:
	pipenv run yapf --recursive --in-place

################################################
#              Running the app                 #
################################################

debug:
	python app.py --debug

run:
	gunicorn -k eventlet -w 1 --bind 0.0.0.0:80 app:app

PID=$(shell cat run.pid)

start_gunicorn:
	/usr/local/bin/gunicorn -k eventlet -w 1 --bind 0.0.0.0:80 app:app > /dev/null 2.&1 & echo $$! > run.pid

start:
	/usr/bin/python app.py > /dev/null 2>&1 & echo $$! > run.pid

stop:
	kill ${PID}
