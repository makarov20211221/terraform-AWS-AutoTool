# terraformTest
Terraform Testing Task
Description

Task Testing
Environment

Ubuntu 16.0 Python 3.7 Terraform 0.11.8
Dependency:

boto3 moto
Process description

    Terraform apply resources and IAM Role with permission 2) --> Create Notification 3) --> Create AWS Lambda (Fetching Event Notification and trigger Log & DynamoDB Insertion)

Installation

    Reset the config.tf (id and Key) , Reset the id and key in run.py
    zip -r function.zip run.py
    terraform init --> terraform plan --> terraform apply

Mock

    pip3 install moto
    python3 run_test.py

Real_env Testing

    Reset the config.tf (id , Key and Account_id) , Reset the configs in run.py
    zip -r function.zip run.py
    terraform init --> terraform plan --> terraform apply
    python3 real_env_test.py

Automatically add and delete an Object from the S3 bucket and fecth the logs and DynamoDB Data
Gitee Feature

    You can use Readme_XXX.md to support different languages, such as Readme_en.md, Readme_zh.md
    Gitee blog blog.gitee.com
    Explore open source project https://gitee.com/explore
    The most valuable open source project GVP
    The manual of Gitee https://gitee.com/help
    The most popular members https://gitee.com/gitee-stars/
