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
2.ApacheServer.yaml
ApacheServer.yaml using the ApacheServer-params.json file as the input. 
It creates the webservers which include the Load Balancer, 
AutoScaling Groups and Security Groups are created using 

Instructions(Windows 10 )
First create the network by running the create.bat file as below:

create.bat ApacheNetStack Network.yaml network-params.json

Second Create the Web Stack by running the create file as shown below.

create.bat ApacheWebStack ApacheServer.yaml ApacheServer-params.json

Finally go to "cloudformation"-->"Stacks"--"ApacheWebStack"--"Outputs",
You can get the "LoadBalancerURL",copy the value into your webbrowser.
You will see the website.
URL:
http://apach-WebAp-ARNYONP950OD-1433375166.us-west-2.elb.amazonaws.com






