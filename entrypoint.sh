#!/bin/bash
set -e # exit immediately if a command exits with a non-zero status
cd weather_app
python manage.py migrate
python manage.py runserver 0.0.0.0:8000