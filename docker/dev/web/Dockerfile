# Official Python runtime as the base image
FROM python:3.9.6-buster

# Add metadata to the image
LABEL author="Wayne Lambert <contact@waynelambert.dev>" \
    version="2021.08" \
    description="Docker image for web service of portfolio site."

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Causes all output to stdout to be flushed immediately
ENV PYTHONUNBUFFERED 1

# Set the COLUMNS variable for the terminal's output width
ENV COLUMNS 133

# Install Watchman File Watching Service
RUN cd /tmp \
    && git clone https://github.com/facebook/watchman.git -b v4.9.0 --depth 1 \
    && cd watchman \
    && ./autogen.sh \
    && ./configure --enable-statedir=/tmp --enable-lenient --without-pcre \
    && make -j6 \
    && make install

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

# Bring up the Django development server
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8001" ]
