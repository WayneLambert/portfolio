# Use Alpine version of the Python runtime as the base image
FROM python:3.7.4-alpine

# Add metadata to the image
LABEL author="Wayne Lambert <contact@waynelambert.dev>" \
    version="2019.07" \
    description="Docker image for web service of portfolio site."

# Create and set working directory
WORKDIR /code

# Install additional project dependencies
RUN apk --update add \
    build-base \
    gettext \
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
RUN pipenv install --system --ignore-pipfile --deploy

# Copy local source code directory to container's source code directory
COPY . . 

# Exposes port 8080
EXPOSE 8080

# Starts up the Gunicorn application server on port 8080
CMD ["gunicorn", "--workers=3", "ab_back_end.wsgi:application", "--bind 0.0.0.0:8080"]