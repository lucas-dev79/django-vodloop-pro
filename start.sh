#!/bin/bash

python manage.py migrate
gunicorn podcast.wsgi