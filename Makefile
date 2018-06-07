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
	pipenv run flake8 --ignore=E501 app.py gammabox
	pipenv run pylint app.py gammabox

format:
	pipenv run yapf --recursive --in-place -vv --style google .

################################################
#              Running the app                 #
################################################

debug:
	pipenv run python app.py --debug

run:
	pipenv run gunicorn -k eventlet -w 1 --bind 0.0.0.0:8080 app:app

PID=$(shell cat run.pid)

start_gunicorn:
	pipenv run gunicorn -k eventlet -w 1 --bind 0.0.0.0:8080 app:app > /dev/null 2.&1 & echo $$! > run.pid

start:
	pipenv run python app.py > /dev/null 2>&1 & echo $$! > run.pid

stop:
	kill ${PID}
