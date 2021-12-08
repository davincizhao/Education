# 1. What is DevOps?
## DevOps
DevOps is the combination of industry best practices, and set of tools that improve an organization’s ability to:

- Increase the speed of software delivery
- Increases the speed of software evolution
- Have better reliability of the software
- Have scalability using automation,
- Improved collaboration among teams.
- In other words, these tools enable a company to showcase industry best practices in software development.

**Devops Diagram from StackExchange**
![devops](https://i.stack.imgur.com/kEOe7.png)

## Issues that DevOps tries to solve:
- Unpredictable deployments
- Mismatched environments (development doesn’t match production)
- Configuration Drift


## DevOps best practices and tools
One of the benefits of using DevOps is that it allows predictable deployments using automated scripts. In the DevOps model, development and operations teams are merged into a single team. These DevOps teams use a few tools and best practices that deploy and manage configuration changes to servers. Stackexchange has a discussion post detailing the difference between DevOps tools vs. Software Configuration Tools.

The most important practices are:

- **Continuous Integration / Continuous Delivery (CI/CD)** - new features are automatically deployed with all the required dependencies.
- **Infrastructure as Code (IaaC)** - configuration and management of cloud infrastructure using re-usable scripts.
Other prevalent practices are:

- Microservices
- Monitoring and Logging
- Communication and Collaboration

### Glossary
- **Continuous Integration Continuous Deployment (CI/CD):** Tracks the development workflow from testing through production. Continuous integration is the process flow of testing any change made to your development flow, while continuous deployment tracks those changes through to staging and production systems. You may like to read this article by Atlassian.com that describes CI/CD in detail.
- **Infrastructure as code (IaC):** Provision and manages the cloud-infrastructure by using scripts. These scripts can be written in YAML or JSON format. These scripts ensure that the same architecture can be re-built multiple numbers of times. These scripts are particularly useful in enterprise applications and different environments - dev, prod, or test. 



## What is CloudFormation?
**CloudFormation** is an AWS tool for creating, managing, configuring, and deploying cloud resources. This tool is beneficial if you have to provision a set of cloud resources multiple times, at scale. You can do so by simply writing **(YAML or JSON)** scripts that you can easily edit and run numerous times. In the script, we mention each resource's necessary configuration that we want to provision and then use the AWS CLI tool and commands to execute the scripts.
### CloudFormation
CloudFormation is a declarative language, not an imperative language.
CloudFormation handles resource dependencies so that you don’t have to specify which resource to start up before another. There are cases where you can specify that a resource depends on another resource, but ideally, you’ll let CloudFormation take care of dependencies.
VPC is the smallest unit of resource.

#### Glossary
- **Name:** A name you want to give to the resource (does this have to be unique across all resource types?)
- **Type:** Specifies the actual hardware resource that you’re deploying.
- **Properties:** Specifies configuration options for your resource. Think of these as all the drop-down menus and checkbox options that you would see in the AWS console if you were to request the resource manually.
- **Stack:** A stack is a group of resources. These are the resources that you want to deploy, and that are specified in the YAML file.

- **Declarative languages:** These languages specify what you want, without requiring you to specify how to get it. An example of a popular declarative language is SQL.
- **Imperative languages:** These languages use statements to change the state of the program.

### YAML and JSON
- YAML and JSON file formats are both supported in CloudFormation, but YAML is the industry preferred version that’s used for AWS and other cloud providers (Azure, Google Cloud Platform).

- An important note about YAML files: the whitespace indentation matters! We recommend that you use four white spaces for each indentation.

### Best practices
Create separate files to organize your code. You can either create separate files for similar resources or create files for each developer who uses those resources.

## Config AWS CLI
After installing AWS CLI, recall that you must configure the following four items on your local machine before you can interact with any of the AWS services:

- **Access key** - It is a combination of Access Key ID and a Secret Access Key. You can generate an Access key from the AWS IAM service, and specify the level of permissions (authorization) with the help of IAM Roles.
- **Default AWS Region** - It specifies the AWS Region where you want to send your requests by default.
- **Default output format** - It specifies how the results are formatted. It can either be a json, yaml, text, or a table.
- **Profile** - A collection of settings is called a profile. The default profile name is default, however, you can create a new profile using the aws configure --profile new_name command.


### Deciding Access Privileges within AWS
#### AWS access type
- **Programmatic Access:** In the AWS console, choose "programmatic access." This allows us to use code to interact with AWS, instead of relying on mouse clicking in the console web pages. Choosing this option will Enable the access key ID and secret access key for the AWS CLI.
- **AWS Management Console access:** it is used only when you want the new user to be able to sign-in to the AWS web console using a password. This one is not the case in our course
#### Permissions
- **Administrator Access:** The permissions to a user are granted in form of Policies, which are JSON documents. The AWS web console provides a pre-created list of policies to choose from. For the current IAM user that you are creating, choose “administrator access.” This is just for the initial setup of your account. Afterward, you’ll want to limit access to only what you need.


### Development and Production user accounts
In practice, Development and DevOps members may have separate user accounts for the development environment as opposed to the production environment. This makes it easier for developers by giving them wider privileges in the dev environment that would normally only be reserved for DevOps members in the production environment.

## Create Cloudformation stack
### Create stack
- **Create the template file:** Use the following code for your first test file: demo_cf.yml (or choose any other name). Be careful about the indentation while you paste/write the same code in your editor.

```
AWSTemplateFormatVersion: 2010-09-09
Description: demo show template deploys a VPC
Resources:
UdacityVPC:
  Type: 'AWS::EC2::VPC'
  Properties:
    CidrBlock: 10.0.0.0/16
    EnableDnsHostnames: 'true'
    Tags:
    - Key: name
      Value: demovpc
```

- **Run the aws command :** Run the following command in the terminal, from the same directory where you've placed your testcfn.yml file.
```
aws cloudformation create-stack  --stack-name myCFStack --region us-east-1 --template-body ./demo_cf.yml
```

- **Alternate method - Shell Script:** You can write a shell script (.sh) file as:
```
aws cloudformation create-stack --stack-name $1 --template-body file://$2  --parameters file://$3 --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" --region=us-west-2
```

- **Alternate method - Batch Script** You can also try a batch script (.bat) with a similar syntax, except that the actual values can be written as``` %1``` instead as```$1```.

### Update stack
You may also want to use update-stack when you want to update an existing stack instead of destroying your stack and creating a new one. The syntax is similar to before:
```
aws cloudformation update-stack --stack-name $1 --template-body file://$2  --parameters file://$3 --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" --region=us-west-2
```

### Describe stack
Once a stack is created successfully, you can verify by either going to the web console or running the following command, which will display all the details the stack.
```
aws cloudformation describe-stacks --stack-name demo_cf.yml
```
