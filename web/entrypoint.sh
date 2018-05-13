#!/bin/env bash
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
nohup python /data/web/manage.py process_tasks --log-std &
gunicorn app.wsgi:application -w 2 -b :80
