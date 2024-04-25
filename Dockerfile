# Use an official Python 3.11 runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container's working directory
COPY . /app

# Install Poetry
RUN pip install poetry

# Configure Poetry to not create a virtual environment
# and to not ask any interactive question
RUN poetry config virtualenvs.create false \
    && poetry config installer.parallel false

# Install project dependencies
RUN poetry install --no-dev

# Install cron first
RUN apt-get update && apt-get -y install cron && apt-get install -y procps

# Install bash
RUN apt-get -y install bash

RUN apt-get install systemctl

# Setup cron job
COPY crontab /etc/cron.d/bot-cron
RUN chmod 0644 /etc/cron.d/bot-cron
RUN crontab /etc/cron.d/bot-cron

# Run the command on container startup
CMD cron -f
