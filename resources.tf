terraform {
  backend "local" {
    path = "./terraform.tfstate"
  }
}

provider "aws" {
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region     = "${var.aws_region}"
}

# Create DynamoDB Resource
resource "aws_dynamodb_table" "table" {
  provider = "aws"

  name             = "remove_logs"
  hash_key         = "object_name"
  range_key        = "deleted_at"
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"
  read_capacity    = 1
  write_capacity   = 1

  attribute = [{
    name = "object_name"
    type = "S"
  },
    {
      name = "deleted_at"
      type = "N"
    },
  ]
}

# Create IAM 
resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow"
    }
  ]
}
EOF
}

# IAM_Role_Policy

resource "aws_iam_role_policy" "lambda-cloudwatch-log-group" {
  name = "kzonov-cloudwatch-log-group"
  role = "${aws_iam_role.iam_for_lambda.name}"

  policy = "${data.aws_iam_policy_document.cloudwatch-log-group-lambda.json}"
}

data "aws_iam_policy_document" "cloudwatch-log-group-lambda" {
  statement {
    sid = "1"

    actions = [
      "logs:*",
      "dynamodb:*",
	  "s3:*"
    ]
    
	# Test-stage config. In real_env replace "*" with "${var.aws_account_id}"
    resources = [
    "arn:aws:cloudwatch:us-east-1:*:*",
    "arn:aws:logs:us-east-1:*:*",
    "arn:aws:dynamodb:us-east-1:*:table/*",
    "arn:aws:lambda:us-east-1:*:function:record_remove_object_on_s3",
    "arn:aws:s3:::${var.bucket_name}"
    ]


    effect = "Allow"
  }
}


resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.func.function_name}"
  principal     = "s3.amazonaws.com"
  source_arn    = "${aws_s3_bucket.bucket.arn}"
}

resource "aws_lambda_function" "func" {
  filename      = "run.zip"
  function_name = "record_remove_object_on_s3"
  role          = "${aws_iam_role.iam_for_lambda.arn}"
  handler       = "run.lambda_handler"
  runtime       = "python3.7"
}

resource "aws_s3_bucket" "bucket" {
  bucket = "${var.bucket_name}"
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = "${aws_s3_bucket.bucket.id}"

  lambda_function {
    lambda_function_arn = "${aws_lambda_function.func.arn}"
    events              = ["s3:ObjectRemoved:*"]
  }
}

resource "aws_cloudwatch_log_group" "group_test" {
  name = "group_test"
}

resource "aws_cloudwatch_log_stream" "stream_test" {
  name           = "stream_test"
  log_group_name = "${aws_cloudwatch_log_group.group_test.name}"
}
