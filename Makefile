# Makefile Corrigido
setup:
	docker compose up --build

run:
	docker compose up

test:
	docker compose exec web python manage.py test

seed:
	docker compose exec web python manage.py seed