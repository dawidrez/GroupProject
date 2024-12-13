FROM python:3.13.0-slim-bookworm

WORKDIR /app

COPY ./docker/scripts /scripts
RUN find /scripts -type f -exec chmod +x {} \;

COPY . .


RUN pip install --no-cache-dir -r requirements.txt

