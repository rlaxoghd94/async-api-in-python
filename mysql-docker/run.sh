#!/bin/sh
CONTAINER_NAME=mysql-docker
if [ ! "$(docker ps -a -q -f name=${CONTAINER_NAME})" ]; then
	if [ "$(docker ps -aq -f status=exited -f name=${CONTAINER_NAME})" ]; then
		# cleanup
		docker kill ${CONTAINER_NAME}
		docker container prune -f
	fi
	
	# run container
	# docker run -d -p 1521:1521 -p 81:81 -v ../api-server/h2-data -e H2_OPTIONS=-ifNotExists --name=${CONTAINER_NAME} oscarfonts/h2 --platform=linux/arm64/v8
	# docker run -d -p 5432:5432 --name $CONTAINER_NAME -e POSTGRES_PASSWORD=mysecretpassword postgres
	docker run --name ${CONTAINER_NAME} -p 3306:3306 -e MYSQL_ROOT_PASSWORD=q1w2e3 -d mysql
fi

