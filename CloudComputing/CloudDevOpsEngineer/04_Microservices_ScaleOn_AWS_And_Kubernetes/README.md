# 1. What is Microservices?

## Why FaaS?
- Higher developer ROI because server infrastructure management no longer required.
- More time focused on writing code, which leads to a higher developer velocity.
- Functional programming is a design well suited to distributed computing. Instead of scaling your entire application, you can scale your functions automatically and independently with usage.
## AWS lambda(Fuctions as a Service) FaaS?
AWS Lambda is a **compute service** that lets you run code **without provisioning or managing servers**.

- "AWS Lambda executes your code only when needed and scales automatically, from a few requests per day to thousands per second.
You pay only for the compute time you consume - there is no charge when your code is not running."
- "You can use AWS Lambda to run your code in response to events," such as HTTP requests.

## SQS Queue
**Amazon Simple Queue Service (Amazon SQS)** offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components.

- A **queue** is just a type of list that orders data in a particular way; typically in a first-item-in = first-item-out order (FIFO), as shown below.

## Type of Serverless
- Amazon Web Services [ Chalice & Cloud Formation]
- Terraform
- Google Cloud Platform
- Microsoft Azure

## Cloud Native Computing
### Defination from Cloud Native Computing Foundation:
Cloud Native computing empower organizations to build and run scalable applications in modern, dynamic environments such as public, private, and hybrid clouds. Containers, service meshes, microservices, immutable infrastructure, and declarative APIs exemplify this approach.

### Benefits of Cloud Computing
#### Cost
There is no up-front cost and resources can be precisely metered to meet demand.
Speed
The cloud offers self-service, so an expert user can leverage the resources to build solutions quickly.
#### Global scale
All major cloud providers have a global scale, which means services can be provisioned all over the world to meet demand in a geographic region.

#### Productivity
Many tasks, such as racking servers, configuring network hardware, and physically securing a data center, no longer exists. Companies can focus on building core intellectual property versus reinventing the wheel.

#### Performance
The performance of applications can leverage a continuous upgrade cycle. The network, the storage and the compute improve over time consistently. Additionally, Cloud-Native applications are able to leverage new capabilities in the cloud to further increase performance.

#### Reliability
The core architecture of the cloud offers redundancy at every step. There are multiple regions and multiple data centers in each region. Cloud-native architecture can design around these capabilities, leading to highly available architectures. Additionally, many-core cloud services are themselves highly available, like Amazon S3, which has nine nines, or 99.999999999% reliability.

#### Security
You are only as good as your weakest link with security. By consolidating to centralized security, a higher level of security occurs. Problems such as physical access to a data center or encryption at rest become industry standard on day one.






# 2. Operationalize a Machine Learning Microservice API.
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




