#!/bin/bash
source ./deploy_scripts/setup.sh

gcloud run deploy selenium-chrome-standealone\
    --image=gcr.io/$PROJECT_ID/selenium\
    --platform managed --port=4444:8080