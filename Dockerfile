# Official Python runtime as the base image
FROM python:3.7.3-alpine

RUN apk --update add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq \
    gettext \
    nginx \
    # Pillow dependencies
    jpeg-dev \
    zlib-dev

# Set working directory
WORKDIR /code

# Add metadata to the image
LABEL author="Wayne Lambert <contact@waynelambert.dev>" \
    version="2019.07" \
    description="Docker image for portfolio site. Hosted at https://waynelambert.dev"

# Install pipenv from PyPI
RUN pip install pipenv

# Copy local files to container
COPY Pipfile Pipfile.lock /code/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy --dev

# Copy the contents of code folder locally to the code directory in container
COPY . .

# Run script file.
CMD ./run-dev.sh