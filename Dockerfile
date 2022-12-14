# Official Python runtime as the base image
FROM python:3.10.8-buster

# Add metadata to the image
LABEL dev.waynelambert.author="Wayne Lambert <wayne.a.lambert@gmail.com>" \
    dev.waynelambert.version="2022.12" \
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
RUN curl -sSL https://install.python-poetry.org | python3

# Set Poetry in the container's $PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy the package management files into the container
COPY pyproject.toml poetry.lock ./

# Do not create a virtual environment
RUN poetry config virtualenvs.create false

# Install Poetry packages and dependencies (excluding dev packages)
RUN poetry install --no-dev --no-interaction --no-ansi --no-root

# Copy local source code directory to container's source code directory
COPY . .

# Add a new group for the app
ARG APP_GROUP=app-grp
RUN groupadd ${APP_GROUP}

# Add new user for app
ARG APP_USER=app-usr
RUN useradd --create-home --gid ${APP_GROUP} ${APP_USER}

# Recursively change the user:group of the directory
RUN chown -R ${APP_USER}:${APP_GROUP} .

# Change the user to the application user (i.e. non-root access)
USER ${APP_USER}

CMD [ "python", "manage.py", "collectstatic", "--noinput", "--clear" ]
