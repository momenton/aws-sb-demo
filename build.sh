#!/usr/bin/env bash

docker build -t aws-sb-demo .
docker tag aws-sb-demo:latest 841938870680.dkr.ecr.ap-southeast-2.amazonaws.com/aws-sb-demo:latest
eval $(AWS_PROFILE=momenton-melchi aws ecr get-login --no-include-email --region ap-southeast-2)
docker push 841938870680.dkr.ecr.ap-southeast-2.amazonaws.com/aws-sb-demo:latest