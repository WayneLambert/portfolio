# Official Python runtime as the base image
FROM python:3.7.4-alpine

# Add metadata to the image
LABEL author="Wayne Lambert <contact@waynelambert.co.uk>" \
    version="2019.07" \
    description="Docker image for web service of portfolio site."

# Causes all output to stdout to be flushed immediately
ENV PYTHONUNBUFFERED 1

# Create and set working directory
WORKDIR /code

# Install additional project dependencies
RUN apk --update add \
    build-base \
    gettext \
    nginx \
    # Postgres Dependencies
    libpq \
    --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql \
    postgresql-dev \
    # Pillow dependencies
    jpeg-dev \
    zlib-dev \
    # Install Bash and sudo for a better development shell
    bash \
    bash-doc \
    bash-completion \
    sudo \
    tree \
    --no-cache su-exec

# Install pipenv from PyPI
RUN pip install pipenv

# Copy local files to container
COPY Pipfile Pipfile.lock /code/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy --dev

# Copy local source code directory to container's source code directory
COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8001" ]