#!/bin/sh

until cd /app/backend
do
    echo "Waiting for backend volume..."
done

# Execute worker
celery -A backend.celery worker --loglevel=info --concurrency 1 -E