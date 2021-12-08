# Operationalize a Machine Learning Microservice API.
Using Cloud Circle CI to build a Machine Learning Docker API
[Cloud Circle CI Project Link](https://app.circleci.com/pipelines/github/davincizhao/operationalize_ML_Microservice_API)
## Project background
This project goal is to operationalize this working, machine learning microservice using kubernetes, which is an open-source system for automating the management of containerized applications. In this project you will:

- Test your project code using linting
- Complete a Dockerfile to containerize this application
- Deploy your containerized application using Docker and make a prediction
- Improve the log statements in the source code for this application
- Configure Kubernetes and create a Kubernetes cluster
- Deploy a container using Kubernetes and make a prediction
- Upload a complete Github repo with CircleCI to indicate that your code has been tested


## How to run python scripts
cmd: "sudo docker run -it app bash"
cmd: "./make_prediction.sh"

## Explanation of the files
### .circleci/config.yaml : circle ci config file for workflow and pipeline.
### Dockerfile : this is docker configuration file to build and run image.
### Makefile: this is Makefile to setup environment in runtime at first. 
### And test docker's configureation file and pylint to test python script code.
### README.md: this is manual file.
### app.py: basic python code for run in application
### hadolint and kubectl : both are executable file in ubuntu OS
### make_prediction.sh: this is bash shell script to run prediction.
### requirements.txt: requirement libraries for this running enviroment
### run_docker.sh: build docker imager and run it bash script
### run_kubernetes.sh: deploy pod in kubernetes bash script
### upload_docker.sh: upload docker image to cloud bash script




