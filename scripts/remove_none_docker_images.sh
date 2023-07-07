#!Remove none images from computer: 
docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}")
