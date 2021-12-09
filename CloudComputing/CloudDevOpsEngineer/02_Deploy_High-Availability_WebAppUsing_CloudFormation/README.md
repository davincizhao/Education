# Deploy High-Availability Web App using cloudformation
The Deploy a high-availability web app using using Cloudformation 

project for the Udacity Devops Nanodegree course.
There are included 
Network.yaml,
network-params.json,
ApacheServer.yaml,
ApacheServer-params.json,
VPC diagram.jpeg,
README.txt: this file 
create.bat: windows script for cloudformation create stack
update.bat: Windows script for cloudformation update stack

**AWS Diagram**
using cloud service www.lucidchart.com to draw project Diagram

![Diagram](https://github.com/davincizhao/Education/blob/main/CloudComputing/CloudDevOpsEngineer/02_Deploy_High-Availability_WebAppUsing_CloudFormation/VPC%20diagram.jpeg)

## 1. Network.yaml：

The Network.yaml file is for creating the network VPC, Subnets etc. using the network-params.json as input parameters. 
AWS resources define in yaml format:
- 1 VPC
- 1 InternetGateway
- 1 InternetGatewayAttachment, for attach the InternetGateway to VPC
- 1 PublicSubnet1 and 1 PublicSubnet2
- 1 PrivateSubnet1 and 1 PrivateSubnet2
- 1 NatGateway1EIP and 1 NatGateway2EIP, for Elastic IP, not need to change IP.
- 1 NatGateway1 and 1 NatGateway2, Allocate with each EIP
- 1 PublicRouteTable 
- 1 DefaultPublicRoute, all outbond trafic(destination:0.0.0.0/0) will send to InternetGateway
- 1 PublicSubnet1RouteTableAssociation and 1 PublicSubnet2RouteTableAssociation, for Association public route table to public subnet1 and public subnet2 
- 1 PrivateRouteTable1 and 1 PrivateRouteTable2
- 1 DefaultPrivateRoute1 and 1 DefaultPrivateRoute2, all trafic(destination:0.0.0.0/0) will send to NatGateway1 or NatGateway2
- 1 PrivateSubnet1RouteTableAssociation and 1 PrivateSubnet2RouteTableAssociation, for Association Private route table to Private subnet1 and Private subnet2

Code sample
```
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCIDR
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
      - Key: Name
        Value: !Ref EnvironmentName

  InternetGateway:
    Type: AWS::EC2::InternetGateway

  InternetGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment

  PublicSubnet1:
    Type: AWS::EC2::Subnet


  PublicSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 1, !GetAZs  '' ]
      CidrBlock: !Ref PublicSubnet2CIDR
      MapPublicIpOnLaunch: true

  PrivateSubnet1:
    Type: AWS::EC2::Subnet

  PrivateSubnet2:
    Type: AWS::EC2::Subnet


  NatGateway1EIP:
    Type: AWS::EC2::EIP
    DependsOn: InternetGatewayAttachment
    Properties:
      Domain: vpc

  NatGateway2EIP:
    Type: AWS::EC2::EIP


  NatGateway1:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt NatGateway1EIP.AllocationId
      SubnetId: !Ref PublicSubnet1

  NatGateway2:
    Type: AWS::EC2::NatGateway

  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName} Public Routes

  DefaultPublicRoute:
    Type: AWS::EC2::Route
    DependsOn: InternetGatewayAttachment
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway

  PublicSubnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PublicRouteTable
      SubnetId: !Ref PublicSubnet1

  PublicSubnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation


  PrivateRouteTable1:
    Type: AWS::EC2::RouteTable


  DefaultPrivateRoute1:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PrivateRouteTable1
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGateway1

  PrivateSubnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation


  PrivateRouteTable2:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName} Private Routes (AZ2)

  DefaultPrivateRoute2:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PrivateRouteTable2
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGateway2

  PrivateSubnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
```
## 2.ApacheServer.yaml
ApacheServer.yaml using the ApacheServer-params.json file as the parameters input. 
It creates the webservers which include the Load Balancer, 
AutoScaling Groups and Security Groups are created using cloudformation.

**Loadbalancer Diagram**
![LBS](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/component_architecture.png)

ApacheServer resources in yaml:
- RootRole
- RootInstanceProfile
- LBSecGroup, SecurityGroup for LBS
- WebServerSecGroup, SecurityGroup for Web Server
- WebAppLaunchConfig, startup script to install apache2 and start apache2 service
- WebAppGroup, AutoScalingGroup for web app
- WebAppTargetGroup, TargetGroup for webLBS
- WebAppLB, LoadBalancer for Web app server
- Listener, Listener of LBS
- ALBListenerRule, Rule of Listener
 
 

**Code sample**

```
Resources:
  RootRole:
    Type: 'AWS::IAM::Role'
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: 'Allow'
            Principal:
              Service:
                - 'ec2.amazonaws.com'
            Action:
              - 'sts:AssumeRole'
      Path: '/'
      Policies:
        - PolicyName: 'root'
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: 'Allow'
                Action: '*'
                Resource: '*'

  RootInstanceProfile:
    Type: 'AWS::IAM::InstanceProfile'
    Properties:
      Path: '/'
      Roles:
        - Ref: 'RootRole'

  LBSecGroup: 
    Type: AWS::EC2::SecurityGroup
    Properties:
        GroupDescription: Allow http to our load balancer
        VpcId:
          Fn::ImportValue:
            !Sub "${EnvironmentName}-VPCID"
        SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
        SecurityGroupEgress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
    
  WebServerSecGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
        GroupDescription: Allow http to our hosts
        VpcId:
          Fn::ImportValue:
            !Sub "${EnvironmentName}-VPCID"
        SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0 
        SecurityGroupEgress:
        - IpProtocol: tcp
          FromPort: 0
          ToPort: 65535
          CidrIp: 0.0.0.0/0

  WebAppLaunchConfig:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash
          apt-get update -y
          apt-get install unzip awscli -y
          apt-get install apache2 -y
          systemctl start apache2.service
          cd /var/www/html
          aws s3 cp s3://udacity-demo-1/udacity.zip .
          unzip -o udacity.zip
      ImageId: ami-06f2f779464715dc5
      IamInstanceProfile: 
        Ref: RootInstanceProfile
      SecurityGroups:
      - Ref: WebServerSecGroup
      InstanceType: t3.medium
      BlockDeviceMappings:
      - DeviceName: "/dev/sdk"
        Ebs:
          VolumeSize: '10'

  WebAppGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      VPCZoneIdentifier:
      - Fn::ImportValue:
          !Sub "${EnvironmentName}-PRIV-NETS"
      LaunchConfigurationName:
        Ref: WebAppLaunchConfig
      MinSize: '4'
      MaxSize: '4'
      TargetGroupARNs:
        - Ref: WebAppTargetGroup
  
  WebAppTargetGroup:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      HealthCheckIntervalSeconds: 10
      HealthCheckPath: /
      HealthCheckProtocol: HTTP
      HealthCheckTimeoutSeconds: 8
      HealthyThresholdCount: 2
      Port: 80
      Protocol: HTTP
      UnhealthyThresholdCount: 5
      VpcId:
        Fn::ImportValue:
          Fn::Sub: "${EnvironmentName}-VPCID"

  WebAppLB:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Subnets:
        - Fn::ImportValue: !Sub "${EnvironmentName}-PUB1-SN"
        - Fn::ImportValue: !Sub "${EnvironmentName}-PUB2-SN"
      SecurityGroups:
        - Ref: LBSecGroup

  Listener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      DefaultActions:
      -   Type: forward
          TargetGroupArn: 
              Ref: WebAppTargetGroup
      LoadBalancerArn: !Ref WebAppLB
      Port: 80
      Protocol: HTTP

  ALBListenerRule:
    Type: AWS::ElasticLoadBalancingV2::ListenerRule
    Properties:
      Actions:
      -   Type: forward
          TargetGroupArn: !Ref WebAppTargetGroup
      Conditions:
      -   Field: path-pattern
          Values: [/]
      ListenerArn: !Ref Listener
      Priority: 1
```      

## Instructions(Windows 10 )
- First create the network by running the create.bat file as below:
```
create.bat ApacheNetStack Network.yaml network-params.json
```

- Second Create the Web Stack by running the create file as shown below.
```
create.bat ApacheWebStack ApacheServer.yaml ApacheServer-params.json
```
- Finally go to "cloudformation"-->"Stacks"--"ApacheWebStack"--"Outputs",
You can get the "LoadBalancerURL",copy the value into your webbrowser.
You will see the website.
URL:
http://apach-WebAp-ARNYONP950OD-1433375166.us-west-2.elb.amazonaws.com






