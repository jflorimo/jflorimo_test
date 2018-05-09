# jflorimo_test

## init
cd /project
docker-compose build
docker-compose up -d

## Create migrations
docker exec -it django-api makemigrations
## Apply migrations
docker exec -it django-api migrate
##Collect static files
docker exec -it django-api collectstatic



## PSQL connect with special user
psql -U docker


