FROM python:3.11-alpine3.18

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy

WORKDIR /code/src/grocery_list/
