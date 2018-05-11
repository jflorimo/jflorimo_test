# jflorimo_test

## init
cd /project

docker-compose build

docker-compose up -d

## run

http://localhost/

## psql

docker exec -it jflorimo_test_postgres_1 psql -U docker


## Create migrations
docker exec -it django-api makemigrations
## Apply migrations
docker exec -it django-api migrate
##Collect static files
docker exec -it django-api collectstatic



## PSQL connect with special user
psql -U docker


