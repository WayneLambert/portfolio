# Official Python runtime as the base image
FROM python:3.8.1-buster

# Add metadata to the image
LABEL dev.waynelambert.author="Wayne Lambert <contact@waynelambert.dev>" \
    dev.waynelambert.version="2019.12" \
    dev.waynelambert.description="Docker image for web service"

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Causes all output to stdout to be flushed immediately
ENV PYTHONUNBUFFERED 1

# Create and set working directory
WORKDIR /code

# Install pipenv from PyPI
RUN pip install --upgrade pip && pip install pipenv

# Copy local files to container
COPY Pipfile Pipfile.lock /code/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --ignore-pipfile --deploy

# Copy local source code directory to container's source code directory
COPY . .

CMD [ "python", "manage.py", "collectstatic", "--noinput", "--clear" ]
