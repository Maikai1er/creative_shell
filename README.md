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
