#/bin/sh

echo "Waiting for database to get ready..."
sleep 5

echo "Running migrations..."
poetry run masonite-orm migrate

echo "Seeding database..."
poetry run masonite-orm seed:run Users
poetry run masonite-orm seed:run Messages

echo "Starting application..."
poetry run uvicorn main:app --reload --host=0.0.0.0 --port=80