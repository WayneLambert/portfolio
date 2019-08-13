# Purging and Pruning in Docker

## Check status of all images, containers and volumes

`$ docker system df -v`

## Stop all running containers

`$ docker stop $(docker ps -a -q)`

## Remove a specific container

`$ docker container rm <container-name-or-id>`

## Remove Stopped Containers

`$ docker container prune`

## Remove all containers

`$ docker rm -f $(docker ps -a -q)`

## Remove all images

`$ docker rmi -f $(docker images -a -q)`

## Prune all volumes

`$ docker system prune --volumes -f`

Useful Link: <https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/>
