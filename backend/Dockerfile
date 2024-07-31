ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ENV PYTHONPATH /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    nginx \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

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
