# Use official Nginx image as the base image
FROM nginx:1.17.1-alpine

# Add metadata to the image
LABEL dev.waynelambert.author="Wayne Lambert <contact@waynelambert.dev>" \
    dev.waynelambert.version="2019.07" \
    dev.waynelambert.description="Docker image for nginx service"

# Delete the existing default configuration for nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copy my own custom configuration for nginx into the required server folder
COPY ./docker/prod/nginx/nginx.conf /etc/nginx/conf.d