# Base image fpr Python
FROM python:3.9.7-buster

# Add metadata to the image
LABEL dev.waynelambert.author="Wayne Lambert <admin@waynelambert.dev>" \
    dev.waynelambert.version="2021.09" \
    dev.waynelambert.description="Docker image for web service"

# Create and set working directory
WORKDIR /code

# Upgrade pip
RUN pip install --upgrade pip

# Install the latest version of Poetry
RUN pip install poetry

# Set Poetry in the container's $PATH
ENV PATH = "${PATH}:/root/.poetry/bin"

# Copy the package management files into the container
COPY pyproject.toml poetry.lock ./

# Do not create a virtual environment
RUN poetry config virtualenvs.create false

# Install Poetry packages and dependencies (excluding dev packages)
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy local source code directory to container's source code directory
COPY . .

# Make the entrypoint script executable
RUN chmod +x ./docker/prod/web/entrypoint.prod.sh

# Run entrypoint.prod.sh script
ENTRYPOINT ["./docker/prod/web/entrypoint.prod.sh"]
