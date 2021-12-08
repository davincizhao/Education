# 1. What is Cloud Computing?
## Cloud Computing
Cloud Computing is the delivery of IT resources over the Internet. The cloud is like a virtual data center accessible via the Internet that allows you to manage:
- Storage services likes databases
- Servers, compute power, networking
- Analytics, artificial intelligence, augmented reality
- Security services for data and applications

## Characteristics of Cloud Computing
- Pay as you go - You pay only for what you use and only when your code runs.
- Autoscaling - The number of active servers can grow or shrink based on demand.
- Serverless - Allows you to write and deploy code without having to worry about the underlying infrastructure.

## Types of Cloud Computing
### Infrastructure-as-a-Service (IaaS)
The provider supplies virtual server instances, storage, and mechanisms for you to manage servers.
### Platform-as-a-Service (PaaS)
A platform of development tools hosted on a provider's infrastructure.
### Software-as-a-Service (SaaS)
A software application that runs over the Internet and is managed by the service provider.

## Cloud Deployment Models
### Public Cloud
A public cloud makes resources available over the Internet to the general public.
### Private Cloud
A private cloud is a proprietary network that supplies services to a limited number of people.
### Hybrid Cloud
A hybrid model contains a combination of both a public and a private cloud.

**The hybrid model is a growing trend in the industry for those organizations that have been slow to adopt the cloud due to being in a heavily regulated industry. The hybrid model gives organizations the flexibility to slowly migrate to the cloud.**

## Benefits of Cloud Computing
There are several benefits to the cloud.

- Stop guessing about capacity.
- Avoid huge capital investments up front.
- Pay for only what you use.
- Scale globally in minutes.
- Deliver faster.

# 2. Cloud Based Products On AWS
Amazon Web Services offers a broad set of global cloud-based products.
## AWS cloud-based products
### Analytics
- Quick Sight
- Athena
- Redshift

### Application integration
- Simple Queue Service (SQS)
- Simple Notification Service (SNS)

### Cost management
- AWS Budgets
- Compute services
- Elastic Cloud Compute (EC2)
- Lambda
- Elastic Beanstalk

### Database management services
- MySQL
- Oracle
- SQLServer
- DynamoDB
- MongoDB

### Developer tools
- Cloud 9
- Code Pipeline

### Security services
- Key Management Service (KMS)
- Shield
- Identity and Access Management (IAM)

### Additional Services
- Blockchain
- Machine Learning
- Computer Vision
- Internet of Things (IoT)
- AR/VR

## Global Infrastructure
### Region
A region is considered a geographic location or an area on a map.
### Availability Zone
An availability zone is an isolated location within a geographic region and is a physical data center within a specific region.
### Edge Location
An edge location is as a mini-data center used solely to cache large data files closer to a user's location.
### Additional Information
There are more Availability Zones (AZs) than there are Regions.
There should be at least two AZs per Region.
Each region is located in a separate geographic area.
AZs are distinct locations that are engineered to be isolated from failures.

# 3. Foundational Compute Service On AWS
## Servers In The Cloud
Servers in the cloud have revolutionized the IT industry.

- Scale capacity up and down based on demands.
- Storage, more memory, and computing power can be added as needed.
- Obtain servers in minutes.
- No need for onsite hardware or capital expenses.

## Elastic Cloud Compute
Elastic Cloud Compute or EC2 is a foundational piece of AWS' cloud computing platform and is a service that provides servers for rent in the cloud.

### Pricing Options for EC2
There are several pricing options for EC2.
- On Demand - Pay as you go, no contract.
- Dedicated Hosts - You have your own dedicated hardware and don't share it with others.
- Spot - You place a bid on an instance price. If there is extra capacity that falls below your bid, an EC2 instance is provisioned. If the price goes above your bid while the instance is running, the instance is terminated.
- Reserved Instances - You earn huge discounts if you pay up front and sign a 1-year or 3-year contract.

## Elastic Block Store
Elastic Block Store (EBS) is a storage solution for EC2 instances and is a physical hard drive that is attached to the EC2 instance to increase storage.

### Tips
EBS is found on the EC2 Dashboard.
There are several EBS volume types that fall under the categories of Solid State Drives (SSD) and Hard Disk Drives (HDD).

## Virtual Private Cloud (VPC)
Virtual Private Cloud or VPC allows you to create your own private network in the cloud. You can launch services, like EC2, inside of that private network. A VPC spans all the Availability Zones in the region.

VPC allows you to control your virtual networking environment, which includes:

- IP address ranges
- subnets
- route tables
- network gateways

### Security in VPC
Security in the VPC allows you to have complete control over your virtual networking environment.

- Configure your virtual network with public or private facing subnets
- Launch your servers in the selected network to secure access

### Tips
- The default limit is 5 VPCs per Region. You can request an increase for these limits.
- Your AWS resources are automatically provisioned in a default VPC.
- There are no additional charges for creating and using the VPC.
- You can store data in Amazon S3 and restrict access so that it’s only accessible from instances in your VPC.

## Lambda
### Compute Power In The Cloud
Compute power in the cloud is a faster way to build applications, providing:

- no servers to manage (i.e. serverless)
- ability to continuously scale
- ability to run code on demand in response to events
- pay only when your code runs

### Lambda
AWS Lambda provides you with computing power in the cloud by allowing you to execute code without standing up or managing servers.

### Tips for Lambda
- Lambda is found under the Compute section on the AWS Management Console.
- Lambdas have a time limit of 15 minutes.
- The code you run on AWS Lambda is called a “Lambda function.”
- Lambda code can be triggered by other AWS services.
- AWS Lambda supports Java, Go, PowerShell, Node.js, C#/.NET, Python, and Ruby. There is a Runtime API that allows you to use - other programming languages to author your functions.
- Lambda code can be authored via the console.


## Elastic Beanstalk
Elastic Beanstalks is an orchestration service that allows you to deploy a web application at the touch of a button by spinning up (or provisioning) all of the services that you need to run your application.

### Tips for Elastic Beanstalk

- Elastic Beanstalk can be used to deployed web applications developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker.
- You can run your applications in a VPC.

# 4. Storage and Content Delivery

## Storage in the Cloud
Storage and database services in the cloud provide a place for companies to collect, store, and analyze the data they've collected over the years at a massive scale.
### Storage services
- Durability (guarantees that will not lose the data that you upload to the cloud)
- Availaility (How quickly can acesss the data)
- Scalability (Allows applications to always meet demand seamlessly)

#### Type of Scalability
- Scaling up (Vertical)
- Scaling out (Horizontal)
- Diaganal (Combination of Vertical and Horizontal )


## Storage & Database Services
- Amazon Simple Storage Service (Amazon S3)
- Amazon Simple Storage Service (Amazon S3) Glacier
- DynamoDB
- Relational Database Service (RDS)
- Redshift
- ElastiCache
- Neptune
- Amazon DocumentDB

## S3 & S3 Glacier
Amazon Simple Storage Service (or S3) is an object storage system in the cloud.
### Storage Classes
S3 offers several storage classes, which are different data access levels for your data at certain price points.
- S3 Standard
- S3 Glacier
- S3 Glacier Deep Archive
- S3 Intelligent-Tiering
- S3 Standard Infrequent Access
- S3 One Zone-Infrequent Access

### Tips for S3
S3 is found under the Storage section on the AWS Management Console.
A single object can be up to 5 terabytes in size.
You can enable Multi-Factor Authentication (MFA) Delete on an S3 bucket to prevent accidental deletions.
S3 Acceleration can be used to enable fast, easy, and secure transfers of files over long distances between your data source and your S3 bucket.

## DynamoDB(NoSQL)
DynamoDB is a NoSQL document database service that is fully managed. Unlike traditional databases, NoSQL databases, are schema-less. Schema-less simply means that the database doesn't contain a fixed (or rigid) data structure.

### Tips
- DynamoDB is found under the Database section on the AWS Management Console.
- DynamoDB can handle more than 10 trillion requests per day.
- DynamoDB is serverless as there are no servers to provision, patch, or manage.
- DynamoDB supports key-value and document data models.
- DynamoDB synchronously replicates data across three AZs in an AWS Region.
- DynamoDB supports GET/PUT operations using a primary key.

## Relational Database Service (RDS)
RDS (or Relational Database Service) is a service that aids in the administration and management of databases. RDS assists with database administrative tasks that include upgrades, patching, installs, backups, monitoring, performance checks, security, etc.

### Database Engine Support
- Oracle
- PostgreSQL
- MySQL
- MariaDB
- SQL Server
### Features
- failover
- backups
- restore
- encryption
- security
- monitoring
- data replication
- scalability

## Redshift
Redshift is a cloud data warehousing service to help companies manage big data. Redshift allows you to run fast queries against your data using SQL, ETL, and BI tools. Redshift stores data in a column format to aid in fast querying.

### Tips for Redshift
- Redshift delivers great performance by using machine learning.
- Redshift Spectrum is a feature that enables you to run queries against data in Amazon S3.
- Redshift encrypts and keeps your data secure in transit and at rest.
- Redshift clusters can be isolated using Amazon Virtual Private Cloud (VPC).

## Content Delivery In The Cloud
A Content Delivery Network (or CDN) speeds up delivery of your static and dynamic web content by caching content in an Edge Location close to your user base.

### Benefits of CDN
- The benefits of a CDN includes:
- low latency
- decreased server load
- better user experience

## Cloud Front
CloudFront is used as a global content delivery network (CDN). Cloud Front speeds up the delivery of your content through Amazon's worldwide network of mini-data centers called Edge Locations.

CloudFront works with other AWS services, as shown below, as an origin source for your application:

- Amazon S3
- Elastic Load Balancing
- Amazon EC2
- Lambda@Edge
- AWS Shield

### Tips

- CloudFront ensures that end-user requests are served from the closest edge location.
- CloudFront works with non-AWS origin sources.
- You can use GeoIP blocking to serve content (or not serve content) to specific countries.
- Cache control headers determine how frequently CloudFront needs to check the origin for an updated version your file.
- The maximum size of a single file that can be delivered through Amazon CloudFront is 20 GB.

# 5. Security In The Cloud

As adoption of cloud services has increased, so has the need for increased security in the cloud. The great thing about cloud security is that it not only protects data, it also protects applications that access the data. Cloud security even protects the infrastructure (like servers) that applications run on.

The way security is delivered depends on the cloud provider you're using and the cloud security options they offer.

## AWS WAF
AWS WAF (or AWS Web Application Firewall) provides a firewall that protects your web applications. WAF can stop common web attacks by reviewing the data being sent to your application and stopping well-known attacks.

### Tips for WAF
WAF is found under the Security, Identity, & Compliance section on the AWS Management Console.
WAF can protect web sites not hosted in AWS through Cloud Front.
You can configure CloudFront to present a custom error page when requests are blocked.
AWS WAF is available under a composite dashboard, WAF & Shield, that combines the following three services:

- 1**AWS WAF**: It allows you to protect your web applications from common web exploits by monitoring and controlling the web requests coming to an Amazon API Gateway API, an Amazon CloudFront distribution, or an Application Load Balancer.
- 2**AWS Shield**: It provides continuous DDoS attack detection and automatic mitigations. AWS Shield offers two tiers of protection - Standard and Advanced.
- 3**AWS Firewall Manager**: It allows you to configure and manage firewall rules across accounts and applications centrally.

Within AWS WAF service, you can create Web access control lists (web ACLs) to monitor HTTP(S) requests for AWS resources. You can protect the following types of resources:

- CloudFront distributions
- Regional resources (Application Load Balancer, API Gateway, AWS AppSync)

While creating a web ACL, you add rules, such as conditions like originating IP addresses, that determines whether to allow/block each request.

## AWS Shield
AWS Shield is a managed DDoS (or Distributed Denial of Service) protection service that safeguards web applications running on AWS. AWS Shield offers two tiers of protection - Standard and Advanced.

- Standard tier: Standard AWS Shield is a service that you get "out of the box", it is always running (automatically) and is a part of the free standard tier.
- Advanced tier: If you want to use some of the more advanced features, you'll have to utilize the paid tier.

## Identity & Access Management (IAM)
Identity & Access Management (IAM) is an AWS service that allows us to configure who can access our AWS account, services, or even applications running in our account. IAM is a global service and is automatically available across ALL regions.

AWS IAM service securely controls access to AWS resources by authenticating and authorizing (giving granular permissions) the individual users, applications, or services. Let's watch a demo next.

### 1. IAM User
A user is a unique identifier generated by the IAM service and recognized by all AWS services to grant access to AWS resources. A user can be a person, system, or application that requires access to AWS services. You can generate login credentials and access keys for any user in your account. Roles and policies control the scope (permissions) of a user's access to AWS resources in your account.

### 2. IAM Group
A group collects IAM users with the same level of permissions to access AWS resources. You can attach or detach permissions to a group using access control policies. A group makes it easier to manage IAM users with the same level of permissions.

### 3. IAM Role
A role is simply a set of policies (permissions) to access AWS services. You can assign a role either to an IAM user or an AWS service such as EC2. Creating and storing roles helps to delegate access with defined permissions without sharing long-term access keys.

Difference between an IAM role and an IAM user
An IAM user has permanent credentials that can be used to interact with AWS services directly. In contrast, an IAM role does not have any credentials; hence it cannot make direct requests to AWS services. IAM roles are assumed by authorized entities, such as IAM users, applications, or other AWS services.

### 4. IAM Policy
An access control policy is a JSON file that defines the resource to grant access, level of access, and allowed actions. You can attach a policy to multiple users, groups, or roles to assign permissions to AWS resources.

AWS offers predefined policies that are managed by AWS. You can even create, save, and attach custom policies, as shown below

# 6. Networking
Networks reliably carry loads of data around the globe allowing for the delivery of content and applications with high availability. The network is the foundation of your infrastructure.

Cloud networking includes:

- network architecture
- network connectivity
- application delivery
- global performance
- delivery

## Route 53
Route 53 is a cloud domain name system (DNS) service that has servers distributed around the globe used to translates human-readable names like www.google.com into the numeric IP addresses like 74.125.21.147.

### Features
- scales automatically to manage spikes in DNS queries
- allows you to register a domain name (or manage an existing)
- routes internet traffic to the resources for your domain
- checks the health of your resources
### Tips
- Route 53 is found under the Networking & Content Delivery section on the AWS Management Console.
- Route 53 allows you to route users based on the user’s geographic location.

## Elasticity in the Cloud
One of the main benefits of the cloud is that it allows you to stop guessing about capacity when you need to run your applications. Sometimes you buy too much or you don't buy enough to support the running of your applications.

With elasticity, your servers, databases, and application resources can automatically scale up or scale down based on load.

### EC2 Auto Scaling
EC2 Auto Scaling is a service that monitors your EC2 instances and automatically adjusts by adding or removing EC2 instances based on conditions you define in order to maintain application availability and provide peak performance to your users.

#### Features
- Automatically scale in and out based on needs.
- Included automatically with Amazon EC2.
- Automate how your Amazon EC2 instances are managed.
#### Tips
- EC2 Auto Scaling is found on the EC2 Dashboard.
- EC2 Auto Scaling adds instances only when needed, optimizing cost savings.
- EC2 predictive scaling removes the need for manual adjustment of auto scaling parameters over time.

### Elastic Load Balancing
Elastic Load Balancing automatically distributes incoming application traffic across multiple servers.

Elastic Load Balancer is a service that:

- Balances load between two or more servers
- Stands in front of a web server
- Provides redundancy and performance
#### Tips
- Elastic Load Balancing can be found on the EC2 Dashbaoard.
- Elastic Load Balancing works with EC2 Instances, containers, IP addresses, and Lambda functions.
- You can configure Amazon EC2 instances to only accept traffic from a load balancer.

### 1. Application Load Balancer (ALB)
A simple use case: Assume you are running a microservices-architecture based application. An Application Load Balancer allows you to host the different API endpoints of your application on different servers. The load balancer then redirects the incoming HTTP/HTTP traffic to the suitable server based on the rules you specify in the configuration.

If you choose this option, you will be taken to a six-step process:
- Configure Load Balancer
- Configure Security Settings
- Configure Security Groups
- Configure Routing
- Register Targets
- Review

### 2. Network Load Balancer (NLB)
A Network Load Balancer helps to balance the load on each individual server. Having an NLB becomes essential when your application requires handling millions of requests per second securely while maintaining ultra-low latencies.

This option has a five-step process:

- Configure Load Balancer
- Configure Security Settings
- Configure Routing
- Register Targets
- Review

### 3. Classic Load Balancer (CLB)
It is a previous generation option. You can choose a Classic Load Balancer when you have an existing application running in the EC2-Classic network. You will have to follow a seven-step process to create a CLB:

- Define Load Balancer
- Assign Security Groups
- Configure Security Settings
- Configure Health Check
- Add EC2 Instances
- Add Tags
- Review

# 7. Messaging & Containers
## Messaging in the Cloud
There are often times that users of your applications need to be notified when certain events happen. Notifications, such as text messages or emails can be sent through services in the cloud. The use of the cloud offers benefits like lowered costs, increased storage, and flexibility.

## Simple Notification Service(SNS)
Amazon Simple Notification Service (or SNS) is a cloud service that allows you to send notifications to the users of your applications. SNS allows you to decouple the notification logic from being embedded in your applications and allows notifications to be published to a large number of subscribers.
### Features
- SNS uses a publish/subscribe model.
- SNS can publish messages to Amazon SQS queues, AWS Lambda functions, and HTTP/S webhooks.

### Tips
- SNS is found under the Application Integration section on the AWS Management Console.
- SNS Topic names are limited to 256 characters.
- A notification can contain only one message.

## Queues
A queue is a data structure that holds requests called messages. Messages in a queue are commonly processed in order, first in, first out (or FIFO).

Messaging queues improve:

- performance
- scalability
- user experience

## Simple Queue Service(SQS)
Amazon Simple Queue Service (SQS) is a fully managed message queuing service that allows you to integrate queuing functionality in your application. SQS offers two types of message queues: **standard** and **FIFO**.
### Features
- send messages
- store messages
- receive messages

### Tips
- The Simple Queue Service (SQS) is found under the Application Integration on the AWS Management Console.
- FIFO queues support up to 300 messages per second.
- FIFO queues guarantee the ordering of messages.
- Standard queues offer best-effort ordering but no guarantees.
- Standard queues deliver a message at least once, but occasionally more than one copy of a message is delivered.

## What is a Container?
OS level virtualization allows us to run multiple isolated processes in parallel. A container is an isolated process that consists of the following items, all bundled into one package:

the application code,
the required dependencies (e.g. libraries, utilities, configuration files), and
the necessary runtime environment to run the application.
Each container is an independent component that can run on its own and be moved from environment to environment.

### Benefit of Containers
Containers make it easier for developers to create, deploy, and run applications on different hardware and platforms, quickly and easily.
Containers share a single kernel and share application libraries.
Containers cause a lower system overhead as compared to Virtual Machines.
How to create containers?
Several platforms (called Container runtime/engines) allow us to create containers. A few such platforms are:

- Docker
- CRI-O
- OpenVZ
- Containerd


#### 1. Docker Containers versus Virtual Machines
There are several benefits of using Containers over VMs:

Size: Containers are much smaller than Virtual Machines (VM) and run as isolated processes versus virtualized hardware. VMs can be in GBs while containers are in MBs.
Speed: Virtual Machines can be slow to boot and take minutes to launch. A container can spawn much more quickly typically in seconds.
Composability: Containers are designed to be programmatically built and are defined as source code. Virtual Machines are often replicas of a conventional computer system.

#### 2. Docker
Docker is a (container runtime) tool that helps to build, test, and run containers. You can build containers locally using a command-line utility, Docker Desktop. If there are multiple containers running individual services of an application, you will need to use Docker Compose utility to specify dependent relationships between containers.

#### 3. Docker Image
An image (or Docker image) is a portable auto-generated template that contains a set of instructions to create a container. An image can be instantiated multiple numbers of times to create multiple containers.

#### 4. Dockerfile
A text file containing commands to create an image. In other words, Docker generates images by reading the commands from a Dockerfile.

### What is Elastic Container Service (ECS)?
ECS is an orchestration service used for automating deployment, scaling, and managing of your containerized applications. ECS works well with Docker containers by:

- launching and stopping Docker containers
- scaling your applications
- querying the state of your applications
#### Tips
- You can schedule long-running applications, services, and batch processeses using ECS.
- Docker is the only container-runtime platform supported by Amazon ECS. Other container-runtime tools available in the insdustry are Rocket, LXD, OpenVZ, any a few more.

# 8. AWS Management

## Logging In The Cloud
Logging provides visibility into your cloud resources and applications. For applications that run in the cloud, you will need access to logging and auditing services to help you proactively monitor your resources and applications.

Logging allows you to answer important questions like:

- How is this server performing?
- What is the current load on the server?
- What is the root cause of an application error that a user is seeing?
- What is the path that leads to this error?

## Cloud Trail
Cloud Trail allows you to audit (or review) everything that occurs in your AWS account. Cloud Trail does this by recording all the AWS API calls occurring in your account and delivering a log file to you.
### Features
CloudTrail provides event history of your AWS account activity, including:

- who has logged in
- services that were accessed
- actions performed
- parameters for the actions
- responses returned
- This includes actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.

### Tips
- Cloud Trail is found under the Management & Governance section on the AWS Management Console.
- CloudTrail shows results for the last 90 days.
- You can create up to five trails in an AWS region.

## Cloud Watch
Cloud Watch is a service that monitors resources and applications that run on AWS by collecting data in the form of logs, metrics, and events.

### Features
- There are several useful features:
- Collect and track metrics
- Collect and monitor log files
- Set alarms and create triggers to run your AWS resources
- React to changes in your AWS resources
### Tips
- CloudWatch is found under the Management & Governance section on the AWS Management Console.
- Metrics are provided automatically for a number of AWS products and services.

## Infrastructure as Code
Infrastructure as Code allows you to describe and provision all the infrastructure resources in your cloud environment. You can stand up servers, databases, runtime parameters, resources, etc. based on scripts that you write. Infrastructure as Code is a time-saving feature because it allows you to provision (or stand up) resources in a reproducible way

## Cloud Formation
AWS Cloud Formation allows you to model your entire infrastructure in a text file template allowing you to provision AWS resources based on the scripts you write.

### Tips
- Cloud Formation is found under the Management & Governance section on the AWS Management Console.
- Cloud Formation templates are written using JSON or YAML.
- You can still individually manage AWS resources that are part of a CloudFormation stack.


## AWS Command Line Interface (CLI)
The AWS CLI (or Command Line Interface) allows you to access and control services running in your AWS account from the command line. To use the CLI, simply download, install, and configure it.

