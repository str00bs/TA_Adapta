#/bin/sh

echo "Waiting for database to get ready..."
sleep 5

echo "Running migrations..."
poetry run python manage.py migrate

echo "Creating admin account..."
poetry run python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

echo "Starting application..."
poetry run python manage.py runserver 0.0.0.0:80