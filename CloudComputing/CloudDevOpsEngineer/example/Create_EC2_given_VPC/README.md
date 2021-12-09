# demo of create EC2 with given VPC parameters
- demo.yaml: cloudforamtion file in yaml format to create EC2
- demo-parameters.yaml: given VPC parameters, please replace the "<input ..>" with the values that you're given.

```
aws cloudformation create-stack  --stack-name example --region us-east-1 --template-body demo.yml --parameters demo-parameters.yaml
```
