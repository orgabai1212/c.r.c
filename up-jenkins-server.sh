#!/bin/bash
docker build -t jenkins -f Dockerfile-jenkins .
docker run -d --name server-jenkins-17 -p 8080:8080 -p 50000:50000 -v jenkins-data:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins