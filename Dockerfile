FROM python:3.8.6-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apk update \
    && apk add python3-dev gcc libc-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

# install dependencies
COPY requirements_dev.txt .
RUN pip install -r requirements_dev.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D user
USER user
