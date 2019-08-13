# Remove Dangling Images

`$ docker rmi -f $(docker images -f "dangling=true" -q)`

You can also use the far simpler command:

`$ docker image prune`
