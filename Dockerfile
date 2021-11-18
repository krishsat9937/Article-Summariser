# FROM ubuntu:18.04

# LABEL maintainer="Krishna Kumar <krishsat9937@gmail.com>"

# RUN apt-get update -y && apt-get install -y python-pip python-dev

# COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app

# RUN pip install -r requirements.txt

# COPY . /app

# CMD [ "python", "./app.py" ]

# syntax=docker/dockerfile:1
FROM python:3.7-alpine

LABEL maintainer="Krishna Kumar <krishsat9937@gmail.com>"

WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]


