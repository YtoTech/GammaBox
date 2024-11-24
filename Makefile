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
	pipenv run black .

################################################
#              Running the app                 #
################################################

debug:
	pipenv run python app.py --debug

run:
	pipenv run gunicorn -k eventlet -w 1 --bind 0.0.0.0:9898 app:app

install-systemd-unit:
	sudo cp ./misc/gamma-box.service /etc/systemd/system/
	sudo systemctl daemon-reload
	sudo systemctl enable gamma-box.service
