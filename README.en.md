# terraformTest

#### Description
Task Testing

#### Environment
Ubuntu 16.0
Python 3.7
Terraform 0.11.8

#### Dependency:
boto3
moto

#### Process description

1) Terraform apply resources and IAM Role with permission 
         2) --> Create Notification 
		     3) --> Create AWS Lambda (Fetching Event Notification and trigger Log & DynamoDB Insertion)

#### Installation

1. Reset the config.tf (id and Key) , Reset the id and key in run.py
2. zip -r function.zip run.py
3. terraform init  --> terraform plan --> terraform apply

#### Mock

1. pip3 install moto
2. python3 run_test.py

#### Real_env Testing

1. Reset the config.tf (id , Key and Account_id) , Reset the configs in run.py
2. zip -r function.zip run.py
3. terraform init  --> terraform plan --> terraform apply
4. python3 real_env_test.py 

Automatically add and delete an Object from the S3 bucket and fecth the logs and DynamoDB Data 


#### Gitee Feature

1. You can use Readme\_XXX.md to support different languages, such as Readme\_en.md, Readme\_zh.md
2. Gitee blog [blog.gitee.com](https://blog.gitee.com)
3. Explore open source project [https://gitee.com/explore](https://gitee.com/explore)
4. The most valuable open source project [GVP](https://gitee.com/gvp)
5. The manual of Gitee [https://gitee.com/help](https://gitee.com/help)
6. The most popular members  [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)