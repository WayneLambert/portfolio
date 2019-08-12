#!/bin/bash
docker rmi -f $(docker images -f "dangling=true" -q)