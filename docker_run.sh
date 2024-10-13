#!/bin/bash

# Define image and container names
IMAGE_NAME="voxelbot_image"
CONTAINER_NAME="voxelbot_container"

# Step 1: Build the Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Step 2: Run the Docker container
echo "Running Docker container..."
docker run -d \
  --name $CONTAINER_NAME \
  --volume "$(pwd):/app/" \
  --publish 8080:8080 \
  --restart unless-stopped \
  $IMAGE_NAME \
  python -m voxelbot run # Command to run in container

# Step 3: Output container logs (optional)
echo "Tailing logs for the container..."
docker logs -f $CONTAINER_NAME
