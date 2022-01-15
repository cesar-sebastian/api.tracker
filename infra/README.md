## Entry docker bd

`docker exec -it a123bc007edf bash`

## Run migration

`alembic upgrade head`

## Connect to BD

`docker-compose exec db psql -h localhost -U postgres --dbname=postgres`

\l - list all databases
\d+ - list all tables (relations) in the current database
\c postgres - connect to the postgres database
\d cleanings - describe the cleanings table and the associated columns


## Execute after docker compose was updated

docker-compose up --build