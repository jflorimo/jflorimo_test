FROM python:3-slim

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web
COPY requirements.txt /data/web/

# Setup
#RUN apk update
#RUN apk upgrade

RUN pip3 install ipdb bpython flake8

# Supporting libraries for python modules
RUN apt-get update && apt-get install --yes libpq-dev build-essential postgresql-common gettext

#RUN apk add --update python3 python3-dev postgresql-client postgresql-dev build-base gettext
RUN pip3 install --upgrade pip
RUN pip3 install -U setuptools
RUN pip3 install -r requirements.txt

# Clean
#RUN apk del -r postgresql

# Prepare
COPY ./app /data/web/
RUN mkdir -p /data/web/app/static/admin
