# Use official Nginx image as the base image
FROM nginx:1.17.1

# Delete the existing default configuration for nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copy my own custom configuration for nginx into the required server folder
COPY ./docker/prod/nginx/nginx.conf /etc/nginx/conf.d/nginx.conf