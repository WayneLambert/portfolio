# Use official Postgres image as the base image
FROM postgres:13.4

# Add metadata to the image
LABEL dev.waynelambert.author="Wayne Lambert <admin@waynelambert.dev>" \
      dev.waynelambert.version="2021.09" \
      dev.waynelambert.description="Docker image for `postgres` service in Dev"

# Run the rest of the commands as the 'postgres' user
USER postgres

# Update permissions for the data folder of the Postgres database
RUN chmod 0700 /var/lib/postgresql/data

# Creates a new PostgreSQL database cluster
RUN initdb -D /var/lib/postgresql/data

# Temporarily enable trusted mode so that the postgres user password can be changed/secured
RUN echo "host all  all    0.0.0.0/0  trust" >> /var/lib/postgresql/data/pg_hba.conf

# Allows incoming connections on all available IP interfaces
RUN echo "listen_addresses='*'" >> /var/lib/postgresql/data/postgresql.conf

# Make the database initialization script available and run it
COPY init.sql /docker-entrypoint-initdb.d/

# Ensure security is added back to the Postgres config file
RUN echo "host all  all    0.0.0.0/0  md5" >> /var/lib/postgresql/data/pg_hba.conf
