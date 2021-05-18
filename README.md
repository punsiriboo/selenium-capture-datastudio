# Selenium Capture Datastudio
This git repository is from the medium contents:

## Overview
![](assets/overview.png)

## Architecture Diagram
![](assets/architecture.png)


## Configuration file for Line notification and Dashboard
*** Make sure you have the cookies file exported to private folder
</br>
Please edit file ``` private/config.json ``` before you run:
```
{
    "cookies_json_path": "private/datastudio.google.com.cookies.json",
    "report": {
        "id": "",
        "page": ""
    },
    "notify_token": "",
    "selenium_remote_driver_url": ""
}
```
## How to test locally 

### Start web service with docker :
we have Docker installed locally, we can run this to test it:
```
docker build -t capture_dashboard .
docker run --rm -p 8080:8080 -e PORT=8080 capture_dashboard
```

### Test using curl command :
```
```

## How to deploy to Cloud Run

To deploy please copy sample_setup.sh to private folder and edit your GCP project configuration.
```
cp deploy_scripts/sample_setup.sh  deploy_scripts/setup.sh
```

The runing the deploy script to deploy to your GCP project
```
sh deploy_scripts/cloud_run.sh
```
## Reference
* https://dev.to/googlecloud/using-headless-chrome-with-cloud-run-3fdp