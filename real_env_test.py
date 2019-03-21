#real-env testing
import time

import boto3
import run

LOG_GROUP = run.LOG_GROUP
LOG_STREAM = run.LOG_STREAM
REGION_NAME = run.REGION_NAME
AWS_ACCESS_KEY_ID = run.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = run.AWS_SECRET_ACCESS_KEY
BUECKT_NAME = run.BUECKT_NAME

def real_env_test():

	s3 = boto3.client('s3', 
		region_name = REGION_NAME,
		aws_access_key_id = AWS_ACCESS_KEY_ID,
		aws_secret_access_key = AWS_SECRET_ACCESS_KEY)

	with open('README.en.md', 'rb') as data:
		s3.upload_fileobj(data, BUECKT_NAME , 'object20190320')
		
	s3Response = s3.delete_object(
		Bucket= BUECKT_NAME ,
		Key='object20190320'
	)
	print(s3Response)

	logsClient = boto3.client('logs',    
		region_name = REGION_NAME,
		aws_access_key_id = AWS_ACCESS_KEY_ID,
		aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
		
	logsResponse = logsClient.get_log_events(
		logGroupName='group_test',
		logStreamName='stream_test',
	)
	print(logsResponse)

	dynamodbClient = boto3.client('dynamodb',
		region_name = REGION_NAME,
		aws_access_key_id = AWS_ACCESS_KEY_ID,
		aws_secret_access_key = AWS_SECRET_ACCESS_KEY)

	response = dynamodbClient.scan(
		TableName='remove_logs'
	)
	print(response)

if __name__ == '__main__':
    real_env_test()