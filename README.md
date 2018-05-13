# jflorimo_test

## init
cd /project

docker-compose build

docker-compose up -d

## run

http://localhost/

## IF ISSUE TO RUN FIRST TIME

docker exec -it jflorimo_test_web_1 python manage.py migrate
docker stop jflorimo_test_web_1; docker rm jflorimo_test_web_1; docker-compose up -d;


## POPULATE DATABASE

docker exec -it jflorimo_test_web_1 sh populate.sh

## reboot web

docker stop jflorimo_test_web_1; docker-compose up -d; docker logs jflorimo_test_web_1 -f

## psql

docker exec -it jflorimo_test_postgres_1 psql -U docker

docker=# \c jflorimodb




