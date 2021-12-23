SHELL := /bin/bash

manage_py := python3 ./app/manage.py

run:
	$(manage_py) runserver 0:8000

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

flake8:
	flake8 app/

worker:
	cd app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd app && celery -A settings beat -l info

pytest:
	pytest ./app/tests --cov=app --cov-report html && coverage report --fail-under=89.8344

show-coverage:
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"
