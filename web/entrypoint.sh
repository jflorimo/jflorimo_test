#!/bin/env bash
python manage.py migrate
nohup python /data/web/manage.py process_tasks --log-std &
gunicorn app.wsgi:application -w 2 -b :80
