#!/bin/bash

# Build The Project
echo "Building The Project..."
python3.9 -m pip install -r requirements.txt

# Run The Project
echo "Make Migrations"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static..."
python manage.py collectstatic --noinput --clear