#!/bin/bash

# Install Docker
apt-get update
apt-get install -y docker.io

# Run Docker container
docker run -d -p 5000:5000 gcr.io/ensai-2024/prenom-prediction-api
