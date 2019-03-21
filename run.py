import time

import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

LOG_GROUP = 'group_test'
LOG_STREAM = 'stream_test'
REGION_NAME = 'us-east-1'
AWS_ACCESS_KEY_ID = 'AKIAJQQRCDKIK4GQ27VA'
AWS_SECRET_ACCESS_KEY = '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'
BUECKT_NAME = "mybucket201903210101"

logs = boto3.client('logs', 
    region_name = REGION_NAME,    
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
dynamodb = boto3.resource('dynamodb', 
    region_name = REGION_NAME,
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY)

class Bean(object):
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def log(self):
        logs.put_log_events(
            logGroupName=LOG_GROUP,
            logStreamName=LOG_STREAM,
            logEvents=[
                {
                    'message': self.name,
                    'timestamp': self.time
                }
            ]
        )

    def write(self):
        table = dynamodb.Table('remove_logs')
        with table.batch_writer() as batch:
            batch.put_item(Item={"object_name": self.name, "deleted_at": self.time})


def lambda_handler(event, context):
    print("Event", event)
    print("Context", context)
    logger.info('got event{}'.format(event))
    for record in event['Records']:
        key = record['s3']['object']['key']
        timestamp = int(round(time.time() * 1000))
        bean = Bean(name=key, time=timestamp)
        #bean.log()
        bean.write()

