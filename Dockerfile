# Official Python runtime as the base image
FROM python:3.9.10-buster

# Add metadata to the image
LABEL dev.waynelambert.author="Wayne Lambert <admin@waynelambert.dev>" \
    dev.waynelambert.version="2022.01" \
    dev.waynelambert.description="Docker image for web service"

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Causes all output to stdout to be flushed immediately
ENV PYTHONUNBUFFERED 1

# Create and set working directory
WORKDIR /code

# Upgrade pip
RUN pip install --upgrade pip

# Install the latest stable version of Poetry isolating it from the rest of the system
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Set Poetry in the container's $PATH
ENV PATH = "${PATH}:/root/.poetry/bin"

# Copy the package management files into the container
COPY pyproject.toml poetry.lock ./

# Do not create a virtual environment
RUN poetry config virtualenvs.create false

# Install Poetry packages and dependencies (excluding dev packages)
RUN poetry install --no-dev --no-interaction --no-ansi --no-root

# Copy local source code directory to container's source code directory
COPY . .

CMD [ "python", "manage.py", "collectstatic", "--noinput", "--clear" ]
