#/bin/sh

echo "Waiting for database to get ready..."
sleep 5

echo "Running migrations..."
poetry run python manage.py migrate

echo "Starting application..."
poetry run python manage.py runserver