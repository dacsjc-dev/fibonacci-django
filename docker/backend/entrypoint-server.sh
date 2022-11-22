#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

until python manage.py makemigrations backend --no-input
do
    echo "Waiting for database migrations to be ready..."
done

until python manage.py migrate --no-input
do
    echo "Waiting for database to be ready..."
    sleep 2
done

python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput

gunicorn backend.wsgi:application --bind 0.0.0.0:8000