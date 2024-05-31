# Phishing detection webapp
The application is built using FastAPI framework. 

## How to run the app

The app can be run locally via the [Tox](https://pypi.org/project/tox/) tool. In order to run the app
clone the repo, install Tox and run `tox -e run`. You can also test the app and run linters with the commands
`tox -e test_app` and `tox -e lint` correspondingly.

## Docker

The possibility to run the app via the docker container has been added.
In order to do that first build the docker image using the Dockerfile:

`docker build -t phishing_detection_model:latest .`

After that the app can be run with the following command:

`docker run -p 8001:8001 -e PORT=8001 phishing_detection_model`
