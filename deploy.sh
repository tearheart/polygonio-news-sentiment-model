#!/bin/bash

# Build the Docker image
docker build \
--tag "us-central1-docker.pkg.dev/mlops-3/polygonio-news-sentiment-repo/polygonio-testing-lcd" \
.

# Push image to Google Artifact Registry
#docker push \
#$GCP_ZONE-docker.pkg.dev/$GOOGLE_PROJECT_ID/$ARTIFACT_REPO/$IMAGE_NAME
