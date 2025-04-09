#!/bin/bash

echo ">>> Running migrate"
python manage.py migrate

echo ">>> Starting Gunicorn"
gunicorn podcast.wsgi
