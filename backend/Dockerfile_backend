ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-alpine as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ENV PYTHONPATH /app

RUN apk update && apk add --no-cache \
    build-base \
    nginx \
    postgresql-dev

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN mkdir -p /usr/share/nginx/html/static \
    && chown -R appuser:appuser /usr/share/nginx/html/static

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

USER appuser

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "creative_shell.wsgi", "--bind=0.0.0.0:8000"]
