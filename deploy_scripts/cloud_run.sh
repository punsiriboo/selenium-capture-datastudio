#!/bin/bash
source ./deploy_scripts/setup.sh

# curl https://raw.githubusercontent.com/SeleniumHQ/docker-selenium/trunk/StandaloneChrome/Dockerfile -o Dockerfile
# curl https://raw.githubusercontent.com/SeleniumHQ/docker-selenium/trunk/Standalone/start-selenium-standalone.sh -o start-selenium-standalone.sh
# curl https://raw.githubusercontent.com/SeleniumHQ/docker-selenium/trunk/Standalone/start-selenium-standalone.sh -o selenium.conf
# echo "project id = "$PROJECT_ID
# gcloud config set project $PROJECT_ID
# gcloud config set run/region $COMPUTE_REGION
# gcloud builds submit --tag=gcr.io/$PROJECT_ID/selenium
gcloud run deploy selenium-chrome-standealone\
    --image=gcr.io/$PROJECT_ID/selenium\
    --platform managed --port=4444:8080