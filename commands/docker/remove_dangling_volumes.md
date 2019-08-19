# Remove Dangling Volumes

$ docker volume rm `docker volume ls -q -f dangling=true`
