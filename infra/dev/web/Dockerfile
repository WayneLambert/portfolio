# Pull official Python 3.14.3 runtime as base image
FROM python@sha256:ffebef43892dd36262fa2b042eddd3320d5510a21f8440dce0a650a3c124b51d AS base

# Set shell to bash amd enable 'pipefail' to ensure that if any command in a
# pipe fails (.e.g. curl | gpg), the entire Docker build fails immediately.
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Add metadata to the image
LABEL author="Wayne Lambert <wayne.a.lambert@gmail.com>" \
  version="2026.04" \
  description="Docker image for portfolio."

# Prevents Python from writing .pyc files
# Causes all output to stdout to be flushed immediately
# Set the COLUMNS variable for the terminal's output width
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  COLUMNS=120 \
  DOCKER_CONTENT_TRUE=1 \
  DOCKER_BUILKIT=1


###### ---------- Build `project` stage using `base` as its basis ---------- #####
FROM base AS project

# Set shell to bash amd enable 'pipefail' to ensure that if any command in a
# pipe fails (.e.g. curl | gpg), the entire Docker build fails immediately.
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV COLUMNS=120 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_NO_INTERACTION=1 \
  POETRY_CACHE_DIR=/tmp/poetry-cache

# Create and set working directory
WORKDIR /code

# Upgrade core Python packaging tools to specific versions of build determinism.
# --no-cache-dir: Prevents container from bloating with temporary download files.
RUN python -m pip install --no-cache-dir --upgrade \
  pip==26.0.1 \
  setuptools==82.0.1 \
  wheel==0.46.3

# Install pinned version of Poetry
ENV POETRY_VERSION=2.3.3
RUN curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION

ENV PATH="/root/.local/bin:$PATH"

# Copy the package management files into the container
COPY pyproject.toml poetry.lock ./

# Install Poetry packages and dependencies (including dev packages)
RUN poetry install --no-interaction --no-ansi --no-root


##### ---------- Build 'app' stageusing 'project' as its basis ----------- #####
FROM project AS app

# Add a new group for app
ARG APP_GROUP=pf-grp
RUN groupadd ${APP_GROUP}

# Add new user for app
ARG APP_USER=pf-usr
RUN useradd --gid ${APP_GROUP} ${APP_USER}

# Copy source code into working directory
COPY . .

# Recursively change the user and group of directory
RUN chown -R ${APP_USER}:${APP_GROUP} .

# Change user to application user (i.e. non-root access)
USER ${APP_USER}
