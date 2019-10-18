# Official Python runtime as the base image
FROM python:3.7.3-slim

# Add metadata to the image
LABEL author="Wayne Lambert <contact@waynelambert.dev>" \
    version="2019.10" \
    description="Docker image for web service of portfolio site."

# Causes all output to stdout to be flushed immediately
ENV PYTHONUNBUFFERED 1

# Create and set working directory
WORKDIR /code

# Install pipenv from PyPI
RUN pip install --upgrade pip && pip install pipenv

# Copy local files to container
COPY Pipfile Pipfile.lock /code/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy --dev

# Copy local source code directory to container's source code directory
COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8001" ]