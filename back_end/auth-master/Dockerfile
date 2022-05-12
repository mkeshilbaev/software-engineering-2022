FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED=1
#RUN apt-get update \
#  # dependencies for building Python packages
#  && apt-get install -y build-essential \
#  # psycopg2 dependencies
#  && apt-get install -y libpq-dev \
#  && apt-get install python3-requests
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/