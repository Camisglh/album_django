FROM python:3.9

RUN apt-get update && apt-get install -y \
    postgresql-client

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
