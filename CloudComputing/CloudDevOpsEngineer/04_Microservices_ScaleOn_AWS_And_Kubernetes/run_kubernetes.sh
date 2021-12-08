#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
# dockerpath=<>
pods_name='flaskapp'
dockerpath='davincizhao/udacity_project5'
# Step 2
# Run the Docker Hub container with kubernetes
kubectl run $pods_name --image=$dockerpath   --port=80 --env="DOMAIN=cluster"

# Step 3:
# List kubernetes pods
kubectl get pods
# Step 4:
# Forward the container port to a host
kubectl port-forward $pods_name 8000:80
