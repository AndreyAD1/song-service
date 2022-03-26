FROM python:3.10-slim-buster

WORKDIR usr/src/app

ENV POETRY_VERSION=1.1.13

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . .

ENV FLASK_APP=application.py
