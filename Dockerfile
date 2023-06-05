# syntax=docker/dockerfile:1


FROM python:3.11-slim-buster AS base

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN poetry config virtualenvs.create false 
RUN poetry install --only main --no-interaction --no-ansi --no-root

COPY . .


FROM base AS backend

ENTRYPOINT ["sh", "./entrypoint.sh"]


FROM base AS websocket

ENTRYPOINT ["sh", "./ws_entrypoint.sh"]
