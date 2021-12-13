# 1. What is CI/CD?
**CI/CD Pipeline Diagram**
![cicd](https://github.com/davincizhao/Education/blob/main/CloudComputing/CloudDevOpsEngineer/03_Auto-Deploy_AppWith_Monitoring_Logging/CI_CD.png)

## What is Continuous Delivery
Continuous Delivery is an overarching paradigm or mindset that informs and enhances the practices of Continuous Integration and Continuous Delivery.

**Continuous Integration(CI)** **+** **Continuous Deployment** **=**  **Continuous Delivery**

## Principles of Continuous Delivery
- Repeatable Reliable Process
- Automate Everything
- Version Control Everything
- Bring the Pain Forward
- Build-in Quality
- "Done" Means Released
- Everyone is Responsible
- Continuous Improvement

## Best Practices for CI/CD:
### Fail Fast
Set up your CI/CD pipeline to find and reveal failures as fast as possible. The faster you can bring your code failures to light, the faster you can fix them.

### Measure Quality
Measure your code quality so that you can see the positive effects of your improvement work (or the negative effects of technical debt).

### Only Road to Production
Once CI/CD is deploying to production on your behalf, it must be the only way to deploy. Any other person or process that meddles with production after CI/CD is running will inevitably cause CI/CD to become inconsistent and fail.

### Maximum Automation
If it can be automated, automate it. This will only improve your process!

### Config in Code
All configuration code must be in code and versioned alongside your production code. This includes the CI/CD configuration files!

## Healthy CI Pipelines
- Highest Priority When the Build is Broken
- Trusted Members of the Team
- Have the Same Abilities as any Member of the Team
- Enforce Team Quality Rules
- Communicate Useful Information
- Shorten Feedback Loops
- Don't Require Stacks of Documentation
- Automated to the End!

## Deployment Strategy	
- **Big-Bang**	Replace A with B all at once.
- **Blue Green**	Two versions of production: Blue or previous version and Green or new version. Traffic can still be routed to blue while testing green. Switching to the new version is done by simply shifting traffic from blue to green.
- **Canary**	Aka Rolling Update, After deploying the new version, start routing traffic to new version little by little until all traffic is hitting the new production. Both versions coexist for a period of time.
- **A/B Testing**	Similar to Canary, but instead of routing traffic to new version to accomplish a full deployment, you are testing your new version with a subset of users for feedback. You might end up routing all traffic to the new version, but that's always the goal.

### Blue Green Deployments
#### The Router
**Router Option**
- **Load Balancer**	Instant switch for FE or BE, ideal router in most cases
- **CDN**	Instant switch for front-end web apps.
- **DNS**	A bit slow because of DNS propagation.

#### Step of Blue Green Deployments
- **Integrate Code in a Build**	Compile and create artifact
- **Run Tests**	Run unit and/or integration tests
- **Ensure Infrastructure is Present**	Create green infrastructure
- **Provision the Environment**	Configure green instance, migrate DB, etc
- **Deploy Artifact**	Copy artifact files to instance
- **Run Smoke Tests**	Run a few tests that don't impact the prod server	
- **Perform Rollback if Failure**	Rollback here is more of a cleanup of green
- **Switch Router**	Redirect traffic to new version
- **Run Sanity Test**	Run a few tests that don't impact the prod server
- **Perform Rollback If Failure**	Rollback here is switching the router back to blue and cleaning up green
- **Destroy Old Release Environment?**	Clean up blue env (optional)
- **Notify The Team (Successful)**	Celebrate!


## CI/CD Pipeline Stages
- **Build**	Everything that has to do with making code executable in production (e.g. Compile). The goal is to produce an artifact.
- **Test**	All automated tests that verify at the code level.
- **Analyze**	Any static analysis on the code or checking of dependencies.
- **Deploy**	Anything to do with creating server instances or copying pre-built application files to an instance.
- **Verify**	Any tests that can be run against a running instance of the application, often against a pre-production instance.
- **Promote**	Replacing the current production environment with the new version which was just built and deployed.
- **Revert**	Rolling back or undoing changes in case any verification fails after deployment.

### Stages, Jobs and Steps
- Stages are used to group jobs and control timing.
- Jobs are what actually do the work of CI/CD. Each job has a name and defines a set of instructions to run and an environment in which to run those instructions. 
- The instructions are called steps. Each step has a name and a bit of instructions to carry out a script to execute or a task to complete.

## CI/CD Tools
### Installable/On-Prem
- **Jenkins**	Various Contributors	Vibrant open-source communbity, 100% free
- **Gitlab** Community	Gitlab	Open-source, installable version of the popular cloud-based service, 100% free
- **Team** City	JetBrains	Very mature, JetBrains support
- **Team** Foundation Server (TFS)	Microsoft	Seemless integration with Microsoft products, Microsoft support

### Configuration Management and Automation Tools
- **Chef**	chef.io	Depends on agent to be installed. Very mature.
- **Puppet**	ouppet.com	Requires master "puppet master" server. Performance issues.
- **Salt**	saltstack.com	Keeps inventory on a central server.
- **Ansible**	ansible.com	Most popular. Very fast. Agentless.

### Cloud-Based
- **Bamboo**	Atlassian	Integrates well with other Atlassian products like Stride and Jira.
- **Circle CI**	Circle Internet Services	Free for limited use, personal or business. Boasts of faster builds.
- **Travis CI**	Travis CI	Extremely simple CI/CD orchestration tool. Some specialty features for libraries and packages. Free for open-source projects.
- **GitLab**	GitLab	Complete set of development tools including git repositories and built-in, integrated CI/CD pipelines. 2000 free minutes of CI/CD jobs per month.



## Metrices of CD
- **Lead Time to Production**	(Time at Successful Prod Deployment) - (Time at Completion of Feature Grooming)	Shows how CI/CD is impacting overall delivery time, from the point the team hears about the feature to the point at which it is done (deployed to production). Easy metric to collect if using task management system to track feature grooming and deployments.
- **Rollback Rate**	(Total Rollbacks) / (Total Deployments)	Shows the quality of our deployments. Of course, rate should be low because previous stages should filter out defected builds. This metric is a leading indicator for the confidence of the business in the dev team's ability to delivery.
- **Time to Failure**	(Time at Failure Discovery) - (Time at Build Start)	Shows how quickly we find failures. The lower the better.
- **Production Uptime**	(Total Production Working Time) / (Total Time)	Shows the amount of time we are taking production down because of botched deployments or due to our chosen deployment strategy.
- **Failed Pipeline Cost**	Various calculations including job run time and resources created	Shows the estimated amount of money spent on a failed build. Encourages us to put cheaper jobs earlier in the pipeline.


## Monitoring areas
- Database Stats
- Application Logs
- Docker Logs
- Firewall
- Load Balancer
- GPU
- Operating System
- Router
- Cable Modem
- Message Bus
- AWS Services
- Mail Server
- Other 3rd Party Services
- Other Monitoring Systems

## Key Point of Monitoring
### Availability
Uptime or downtime often translates to dollars, one way or the other. Downtime will increase drastically without monitoring since you won't be watching the system manually, round the clock. This downtime will negatively affect revenue or could increase legal costs.

### Performance
Company performance and image often hangs the reliability of its technology. If systems degrade when users are trying to consume it, their confidence in the system will also degrade, which might result in employee turn-over or loss of clients.

### Capacity
Company or product growth is (generally) a good thing, especially if technology can rise to the demands of its users. But, when infrastructure is not ready meet the needs of business on time, it can result in lost revenue or increased costs.

### Productivity
Development teams who spend time less troubleshooting tend to spend more time developing. However, without proper monitoring, development team members will have no choice but to dive into time-consuming troubleshooting, affecting feature release plans and incurring opportunity costs.

## Reactive vs Proactive
Reactive monitoring is common practice because of its usefulness during a crisis. But, monitoring can have even more power when used proactively.
### Reactive Monitoring
- Real time CPU, memory or disk space meters
- Current health status of any server or resource
- Application logs
- Operating System logs

### Proactive Monitoring
- Forecast Infrastructure Costs
- Monitor the Unknowns
- Track Bugs to Their True Source
- Predict Seasonal Spikes and Trends

## Monitoring System Components
### 1. Time-Series Data
Time-series data is data that is in a series of time intervals. Some examples include:
- Blood-sugar level checked at the top of every hour
- Daily closing value of Microsoft stock
- Monthly rainfall by city
- Available disk space by the minute

### 2. Data Aggregator
A data aggregator is a system that collects and groups data by type or data source. One way to think of data aggregators is like a database with extra tooling to aid in data collection.

### 3. Data Visualizer
A data visualizer takes copious amounts of seemingly unintelligible data from the data aggregator and produces useful charts and graphs.

## Monitoring Tools
### Data Aggregator	###
- **Graphite**	Mature, Open-Source, Installable	Grafana
- **Loggly**	Managed, Cloud-Based, Powerful tooling	Built-In
- **Datadog**	Managed, Cloud-Based, Built-in AI/ML	Built-In
- **Prometheus**	Open Source, Lightweight, Self-Contained, Installable	Grafana
- **Logstash**	Open Source, Cloud-Based or Installable	Kibana
- **CloudWatch**	Built-In to AWS	Built-In

## Exporters in Prometheus
![exporter with prometheus]()
### Available Exporters
- **Node exporter**	Provides basic operating system metrics like CPU, Disk and Memory Usage.
- **Nginx VTS Exporter**	Provides metrics on connections, server zones, and upstream requests.
- **Blackbox exporter**	The Blackbox exporter allows black-box probing of endpoints over HTTP, HTTPS, DNS, TCP, and ICMP
- **Github Exporter**	Provides metrics on repository commits, pull requests, and issues.
- **MongoDB Exporter**	The MongoDB exporter periodically scrapes MongoDB server stats.
- **Jira Exporter**	Provides metrics on Jira issues and projects.
- **Swagger Stats**	API performance stats available to Prometheus
- **AWS Health Exporter**	Provides health metrics on all AWS services and regions.

## Data Visualizer
### Data Visualization Tools
- **Grafana**	Recommended for Prometheus
- **Kibana**	Recommended for Elastic Stack
- **DataDog**	Built in to DataDog cloud-based service
- **Expression Browser**	Built in to Prometheus, okay for experiments

## Alerting Channels
- Email
- Chat Tool
- Desktop Notifications
- Phone Calls


## Helpful Alerting
Alerts should point the way to the source of the problem so that it can be fixed quickly.

- Alerts should always include a brief description of the problem (the easier to understand, the better).
- For code-related issues like run-time exceptions, a stack trace and source code line number is always appreciated.
- When a URL is available to direct the troubleshooting engineer to the problem, it should be included in the alert.




# 2. Auto-Deploy Application With Monitoring and Logging
## Project Scope
- Explain the fundamentals and benefits of CI/CD to achieve, build, and deploy automation for cloud-based software products.
- Utilize Deployment Strategies to design and build CI/CD pipelines that support Continuous Delivery processes.
- Utilize a configuration management tool to accomplish deployment to cloud-based servers.
- Surface critical server errors for diagnosis using centralized structured logging.


## Pre-requirement
Login in CircleCI.com and connect your github with CircleCI.
- 1. select project that you want to work in CircleCI, and press "Set Up Project"
- 2. Create AWS CLI user and role in AWS AIM and save into CircleCI "project setting"
- 3. create new config.yaml or choose from repos ".circleci/config.yaml"

## Propose and Scope the Project
- CI/CD tool platform: CircleCI Cloud,AWS Cloudformation,AWS CLI, AWS EC2, AWS S3,AWS Cloudfront
- Config tool: Ansible
- Monitoring: Prometheus, Altermanager
- Application: NodeJS，NPM
- Repo: Github


## Tools
Tools:
- NPM, package manager for the JavaScript
- CircleCI
- AWS CLI, for AWS command line
- Ansible, for Config the backend server, configure prometheus and node-exporter in backend, deploy "backend artifact" and start npm。
- Prometheus,for monitoring the EC2 backend server.



## Snapshot
### Pre-requirement
1. Set up Github repo with CircleCI
![pre1](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/setup_circleci%20project.png)
2. Save AWS credentials in env in Circle
![cred](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/setp_cred.png)
3. Write and set up config.yml(pipeline jobs and steps)
![pre2](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/setup_ci2.png)
### 1 Build Backend node.js code and find out the error, troubleshooting in build Stage.
![snapshot1](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT01.png)
### 2 Atfer build, Test backend and find out error, troubleshooting.
![snapshot2](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT02.png)
### 3 Build Frontend code and find out the error, Scan front-end dependencies, troubleshooting in build Stage.
![snapshot3](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT03.png)
### 4 Auto send alter to email, when there's fail job or step in CircleCI pipeline. 
![snapshot4](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT04.png)
### 5 Deploy infrastructure (frontend and backend), aws cli,aws cloudformation, etract back-end ip to ansible inventory,Test infrastructure, ensure the backend infrastructure exist
![snapshot5](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT05.png)
### 6 After Deploy, Smoke test both frontend and backend
![snapshot6](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT06.png)
### 7 Smoke test, if there's error, auto destroy enviroments(cloudformation stacks with workflow ID) in AWS and revert migrations.
![snapshot7](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT07.png)
### 8 Smoke test is ok, now Update cloudfront distribution.
![snapshot8](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT08.png)
### 9 Clear up, Remove old stacks and S3 files in AWS 
![snapshot9](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT09.png)
### 10 According to different github branch, run specify jobs, like in build stage, only run "build and test" job in CircleCI
![snapshot10](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT10.png)
### 11 Prometheus: EC2 server in AWS connected to prometheus server
![snapshot11](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT11.png)
### 12 Altermanger,for monitoring backend server status in AWS, auto send alter messages to slack
![snapshot12](https://github.com/davincizhao/Auto_Deploy_Application_with_CircleCI/blob/main/snapshot/SCREENSHOT12_1.png)
