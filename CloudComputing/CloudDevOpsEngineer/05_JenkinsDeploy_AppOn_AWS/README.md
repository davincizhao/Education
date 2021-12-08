# Jenkins Deploy Application On AWS
Using Jenkins(blue ocean) build pipeline and  AWS(Cloud platform) with CloudFormation, AWS CLI,kubectl,eksctl Docker,EKS(Kubenetes in AWS)


## Propose and Scope the Project
- CI/CD tool platform: Jenkins,cloudformation,AWS,AWS Kubernetes as a Service(EKS)
- Deployment strategy: Blue/green deployment.
- Container: Docker.
- Application: Nginx
- Repo: Github


## Tool-box server(Jenkins)
Tools:
- Docker,Container platform
- Jenkins,for CI/CD pipeline platform(JAVA base)
- Kubectl,for Kubernetes cluster command line
- eksctl,for AWS Elastic Kubernetes Services command line
- awscli,for AWS  command line
.

## Repo Structure
There are Two branches **create_cluster** and **app_cicd**: 
- [create_cluster](https://github.com/davincizhao/Capstone-cloud-deploy/tree/create_cluster) for create infrastructure(EKS,Nodegroups) in AWS, 
- [app_cicd](https://github.com/davincizhao/Capstone-cloud-deploy/tree/app_cicd) for test code, build app deploy app to EKS,expose service.
- prepare_jeniks_tools.sh, in [create_cluster] branch for prepare install jenkins and other relative tools, like docker,tidy into Tool-box server

## Prepare Credential of AWS and Dockerhub
- Create user and add EKS permission into this user,save this credential in Jenkins, so that Jenkins can act as user to create EKS.
- Create keypair for login tool-box server(Jenkins) EC2 in AWS.
- Save dockerhub username and password in Jenkins, so that Jenkins can push docker image to dockerhub.

## Screenshot of project
### ss1_setup_jenkins.png
![ss1_setup_jenkins.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss1_setup_jenkins.png)

### ss2_jenkins_install_plugin_blue_ocean.png
![ss2_jenkins_install_plugin_blue_ocean.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss2_jenkins_install_plugin_blue_ocean.png)

### ss3_jenkins_create_EKS_infrastructure.png
![ss3_jenkins_create_EKS_infrastructure.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss3_jenkins_create_EKS_infrastructure.png)

### ss4_jenkins_save_cred_aws_dockerhub.png
![ss4_jenkins_save_cred_aws_dockerhub.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss4_jenkins_save_cred_aws_dockerhub.png)

### ss5_jenkins_setup_pipeline_with_github_repo.png
![ss5_jenkins_setup_pipeline_with_github_repo.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss5_jenkins_setup_pipeline_with_github_repo.png)

### ss6_add_eks_permission_in_aws_user.png
![ss6_add_eks_permission_in_aws_user.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss6_add_eks_permission_in_aws_user.png)

### ss7_create_infr_pipeline_successful.png
![ss7_setup_jenkins.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss7_create_infr_pipeline_successful.png)

### ss8_aws-cloudformation-create_eks-nodegroup-successful.png
![ss8_aws-cloudformation-create_eks-nodegroup-successful.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss8_aws-cloudformation-create_eks-nodegroup-successful.png)

### ss9_tidy_found_html_error.png
![ss9_setup_jenkins.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss9_tidy_found_html_error.png)

### ss10_aws_eks_nodegroup.png
![ss10_setup_jenkins.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss10_aws_eks_nodegroup.png)

### ss11_jenkins_cluster_name_error.png
![ss11_setup_jenkins.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss11_jenkins_cluster_name_error.png)

### ss12_jenkins_app_build_test_push_deply.png
![ss12setup_jenkins.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss12_jenkins_app_build_test_push_deply.png)

### ss13_get_app_a_record.png
![ss13_setup_jenkins.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss13_get_app_a_record.png)

### ss13_get_app_a_record.png
![ss14_setup_jenkins.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss14_blue_deploy_successful.png)

### ss15_switch_lbc_to_green.png
![ss15_setup_jenkins.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss15_switch_lbc_to_green.png)

### ss16_green_deploy_success.png
![ss16_green_deploy_success.png](https://github.com/davincizhao/Capstone-cloud-deploy/blob/master/screenshots/ss16_green_deploy_success.png)
