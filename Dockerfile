# Official Python runtime as the base image
FROM python:3.7

# Set working directory
WORKDIR /src

# Add metadata to the image
LABEL author="Wayne Lambert <contact@waynelambert.dev>" \
    version="2019.07"

# Install pipenv from PyPI
RUN pip install pipenv

# Copy local files to container
COPY Pipfile Pipfile.lock /src/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv sync

# Copy the contents of src folder locally to the src directory in container
COPY . .
