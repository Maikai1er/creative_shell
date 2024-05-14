RUN DOCKER:
docker compose up -d

RUN SERVER:
python manage.py runserver

RUN WORKER:
python -m celery -A creative_shell worker --loglevel=debug

RUN BOT:
python run_bot.py

STOP BOT:
python stop_bot.py

POSTGRES ACCESS:
psql -h localhost -p 5432 -U postgres

NOT
sudo -u postgres psql

SELECT usename FROM pg_user;

\l - DB list

\c - open DB

\d - open table

\q - quit

\dt - see a list of tables in DB

ALTER SEQUENCE cultural_heritage_id_seq RESTART WITH 1;

sudo service PostgreSQL start

docker exec -it <django_container_name> python manage.py migrate

