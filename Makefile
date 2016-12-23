PID=$(shell cat run.pid)

debug:
	python app.py --debug

run:
	gunicorn -k eventlet -w 1 --bind 0.0.0.0:80 app:app

start_gunicorn:
	/usr/local/bin/gunicorn -k eventlet -w 1 --bind 0.0.0.0:80 app:app > /dev/null 2.&1 & echo $$! > run.pid

start:
	/usr/bin/python -u app.py > /dev/null 2>&1 & echo $$! > run.pid

stop:
	kill ${PID}
