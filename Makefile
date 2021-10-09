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

flake8:
	flake8 app/