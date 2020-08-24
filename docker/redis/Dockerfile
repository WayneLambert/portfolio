# Use Alpine version of official Redis image as the base image
FROM redis:6.0.6-alpine

# Add metadata to the image
LABEL com.worksearch.author="Wayne Lambert <contact@waynelambert.dev>" \
    com.worksearch.version="2020.08" \
    com.worksearch.description="Docker image for redis service"

CMD [ "sh", "-c", "exec redis-server --requirepass ${REDIS_PASSWORD}" ]
