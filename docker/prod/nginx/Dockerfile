# Use official Nginx image as the base image
FROM nginx:1.17.1-alpine

# Add metadata to the image
LABEL uk.co.waynelambert.author="Wayne Lambert <contact@waynelambert.co.uk>" \
    uk.co.waynelambert.version="2019.07" \
    uk.co.waynelambert.description="Docker image for nginx service"

# Save a copy of the original config file for reference
# RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.orig

# Delete the existing default configuration for nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copy my own custom configuration for nginx into the required server folder
COPY ./docker/prod/nginx/nginx.conf /etc/nginx/conf.d