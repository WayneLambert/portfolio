# Use Alpine version of the Python runtime as the base image
FROM python:3.8.1-buster

# Add metadata to the image
LABEL dev.waynelambert.author="Wayne Lambert <contact@waynelambert.dev>" \
    dev.waynelambert.version="2019.12" \
    dev.waynelambert.description="Docker image for web service"

# Create and set working directory
WORKDIR /code

# Install pipenv from PyPI
RUN pip install --upgrade pip && pip install pipenv

# Copy local files to container
COPY Pipfile Pipfile.lock /code/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy

# Copy local source code directory to container's source code directory
COPY . .

# Make the entrypoint script executable
RUN chmod +x ./docker/prod/web/entrypoint.prod.sh

# Run entrypoint.prod.sh script
ENTRYPOINT ["./docker/prod/web/entrypoint.prod.sh"]