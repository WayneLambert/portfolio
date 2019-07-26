# Use Alpine version of the Python runtime as the base image
FROM python:3.7.4-alpine

# Add metadata to the image
LABEL uk.co.waynelambert.author="Wayne Lambert <contact@waynelambert.co.uk>" \
    uk.co.waynelambert.version="2019.07" \
    uk.co.waynelambert.description="Docker image for web service"

# Create and set working directory
WORKDIR /code

# Install additional project dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev

# Install pipenv from PyPI
RUN pip install --upgrade pip && pip install pipenv

# Copy local files to container
COPY Pipfile Pipfile.lock /code/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy

# Remove any unrequired build dependencies
RUN apk del build-deps

# Copy local source code directory to container's source code directory
COPY . .

# Make the entrypoint script executable
RUN chmod +x ./docker/prod/web/entrypoint.prod.sh

# Run entrypoint.prod.sh script
ENTRYPOINT ["./docker/prod/web/entrypoint.prod.sh"]