# Configure the AWS Provider
variable "aws_access_key" {
  type    = "string"
  default = "AKIAJQQRCDKIK4GQ27VA"
}

variable "aws_secret_key" {
  type    = "string"
  default = "rQ5oBjviVbj7RDfrJIv7IG2gQAP+aSQv5gZoqAuC"
}

variable "aws_region" {
  type    = "string"
  default = "us-east-1"
}

variable "aws_account_id" {
  type    = "string"
  default = "807374912175 "
}

variable "bucket_name" {
  type    = "string"
  default = "mybucket201903210101"
}

variable "aws_iam_name" {
  type    = "string"
  default = "iam_for_lambda"
}

