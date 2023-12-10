# Official Python runtime as the base image
FROM python:3.11.6 AS base

# Add metadata to the image
LABEL author="Wayne Lambert <wayne.a.lambert@gmail.com>" \
    version="2023.12" \
    description="Docker image for portfolio."

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Causes all output to stdout to be flushed immediately
ENV PYTHONUNBUFFERED 1

# Set the COLUMNS variable for the terminal's output width
ENV COLUMNS 133


###### ---------- Build `project` stage using `base` as its basis ---------- #####
FROM base AS project

# Create and set working directory
WORKDIR /code

# Upgrade pip
RUN pip install --upgrade pip

# Install the latest version of Poetry
RUN pip install poetry

# Copy the package management files into the container
COPY pyproject.toml poetry.lock ./

# Do not create a virtual environment
RUN poetry config virtualenvs.create false

# Install Poetry packages and dependencies (including dev packages)
RUN poetry install --no-interaction --no-ansi

# Copy the source code into working directory
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
