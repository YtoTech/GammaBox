################################################
#                 Installation                 #
################################################

install:
	pipenv install

install-dev:
	pipenv install --dev

################################################
#            Tests & Code analysis             #
################################################

test:
	pipenv run pytest

lint:
	pipenv run flake8 app.py gammabox
	pipenv run pylint app.py gammabox

format:
	pipenv run black .

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
