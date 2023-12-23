#!/usr/bin/env bash
# exit on error
set -o errexit


python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser
mongy
mongy@example.com
f3b4a44410a4d783b4cfa65c69a41a57
f3b4a44410a4d783b4cfa65c69a41a57

python manage.py runscript data
