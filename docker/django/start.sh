#!/bin/bash
# Run migrations

echo Run migrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# Start Gunicorn processes
# echo Starting Gunicorn.
# exec gunicorn admin.wsgi:application \
#    --bind 0.0.0.0:8000 \
#    --workers 3