#!/bin/bash

GOOGLE_PROJECT_ID=mlops-3
GCP_ZONE=us-central1
GCP_BUCKET=polygonio-news-sentiment-test
ARTIFACT_REPO=polygonio-news-sentiment-repo

# Build the Docker image
docker build \
--tag "$GCP_ZONE-docker.pkg.dev$PROJECT_ID/$ARTIFACT_REPO/$IMAGE_NAME" \
.

# Push image to Google Artifact Registry
docker push \
$GCP_ZONE-docker.pkg.dev/$GOOGLE_PROJECT_ID/$ARTIFACT_REPO/$IMAGE_NAME
