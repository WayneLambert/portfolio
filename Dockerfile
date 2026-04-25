# Pull official Python 3.14.3 runtime as base image
FROM python@sha256:ffebef43892dd36262fa2b042eddd3320d5510a21f8440dce0a650a3c124b51d AS base

# Use bash with pipefail so any failed command in a pipeline fails build
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install image dependencies
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    libfontconfig1 \
    libffi-dev \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

# Define build time arguments
ARG APP_GROUP=app-grp
ARG APP_USER=app-usr

# Configure Python and shell output behaviour for container development
ENV COLUMNS=120 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  HOME="/home/${APP_USER}" \
  UV_PROJECT_ENVIRONMENT=/opt/venv \
  PATH=/opt/venv/bin:$PATH \
  DJANGO_SETTINGS_MODULE=aa_project.settings.prod

# Copy uv and uvx binaries from official uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create dedicated non-root group and user for application
RUN groupadd "${APP_GROUP}" && \
  useradd --create-home --gid "${APP_GROUP}" "${APP_USER}"

# Create application and virtual environment directories with correct ownership
RUN mkdir -p /code /opt/venv && \
  chown -R "${APP_USER}:${APP_GROUP}" /code /opt/venv

# Set application working directory
WORKDIR /code

# Run remaining build steps as non-root application user
USER ${APP_USER}

# Copy project dependency files into image
COPY --chown=${APP_USER}:${APP_GROUP} pyproject.toml uv.lock ./

# Sync project environment from the lockfile without dev dependencies
RUN uv sync --locked --no-dev --no-editable --compile-bytecode

# Copy application source code into image
COPY --chown=${APP_USER}:${APP_GROUP} . .

# Run static files collection for application
RUN python manage.py collectstatic --noinput
