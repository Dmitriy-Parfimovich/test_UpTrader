migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

start:
	poetry run python manage.py runserver 127.0.0.1:8000

shell:
	poetry run python manage.py shell

lint:
	poetry run flake8 .

superuser:
	poetry run python manage.py createsuperuser

load:
	poetry run python load_data.py