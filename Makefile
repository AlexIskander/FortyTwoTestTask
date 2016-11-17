PHONY: reload test  syncdb migrate

MANAGE=python $(pwd)manage.py


update:
	@git stash
	@git pull
	@make req
	@make collectstatic
	@make migrate
	@make syncdb
	touch reload_project

reload:
	@make collectstatic
	touch reload

test:
	$(MANAGE)  test

run:
	$(MANAGE) runserver

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

collectstatic:
	$(MANAGE) collectstatic --noinput 

syncdb:
	$(MANAGE) syncdb
	


req:
	@echo "Installing requirements"
	@pip install --exists-action=s -r requirements.txt
