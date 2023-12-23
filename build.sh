#!/usr/bin/env bash
# exit on error
set -o errexit


python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell
from django.contrib.auth.models import User
User.objects.create_superuser(username='mongy', password='f3b4a44410a4d783b4cfa65c69a41a57', email='mongy@example.com')
exit()
python manage.py runscript data
