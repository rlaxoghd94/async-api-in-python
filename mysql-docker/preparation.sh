#!/bin/sh

# check if docker is installed an running
if [ -x "$(command -v docker)" ]; then
    # command
	docker pull mysql
else
    echo "Install docker"
    # command
	exit 1
fi

