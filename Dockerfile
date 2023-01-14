FROM python:3.10.3-slim-buster as poetry_base

ENV POETRY_VERSION=1.2.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_CACHE_DIR=/opt/.cache
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV FLASK_APP=/app/src/random_data_generator/api.py

RUN pip install poetry==${POETRY_VERSION}

WORKDIR /app
COPY poetry.lock pyproject.toml README.md ./
RUN poetry export --output=requirements.txt

FROM python:3.10.3-slim-buster as builder

WORKDIR /app

COPY --from=poetry_base /app/requirements.txt /app/requirements.txt
COPY . ./
RUN pip install -e .

