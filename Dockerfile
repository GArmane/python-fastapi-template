# Python 3.10 Release
FROM python:3.10.1-slim AS base

# Maintainer Information
LABEL maintainer="Giovanni Armane <giovanniarmane@gmail.com>"

# Set environment variables
ENV PYTHON_VERSION=3.10 \
  APP_PATH=/home/python/app \
  POETRY_VIRTUALENVS_CREATE=false \
  PATH=/home/python/.local/lib/python3.10/site-packages:/home/python/.local/bin:/usr/local/bin:/home/python:$PATH

# Install Poetry
RUN pip install --no-cache-dir poetry

# Configure user, groups and working directory
RUN useradd -m -u 1000 -s /bin/bash python && \
  mkdir -p /home/python/app

# Set workdir
WORKDIR /home/python/app

# Expose ports
EXPOSE 8000

# Expose volumes
VOLUME ["/home/python/app"]

# Change user
USER python

# Run the app
CMD ["bash"]

# Development build stage
FROM base AS dev

## Configure Bash
COPY scripts/bash/.bashrc /home/python/.bashrc
ENV ENV="/home/python/.bashrc"

## Copy project file and pre-install
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root

# Production build stage
FROM base AS prod

# Change user back to root
USER root

## Copy application source
COPY . .

# Expose production ports
EXPOSE 8000

## Install dependencies
RUN poetry install --no-dev --no-root
