import time

from moto import mock_logs, mock_dynamodb2

import run


@mock_logs
def test_write_log():
    run.logs.create_log_group(logGroupName=run.LOG_GROUP)
    run.logs.create_log_stream(logGroupName=run.LOG_GROUP, logStreamName=run.LOG_STREAM)

    bean = run.Bean("test", int(round(time.time() * 1000)))
    bean.log()

    response = run.logs.get_log_events(
        logGroupName=run.LOG_GROUP,
        logStreamName=run.LOG_STREAM,
    )
    print(response)
    assert response["events"][0]["timestamp"] == bean.time
    assert response["events"][0]["message"] == bean.name


@mock_dynamodb2
def test_write_ddb():
    run.dynamodb.create_table(
        TableName='remove_logs',
        KeySchema=[
            {
                'AttributeName': 'object_name',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'deleted_at',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'deleted_at',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'object_name',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    bean = run.Bean("test", int(round(time.time() * 1000)))
    bean.write()

    response = run.dynamodb.Table('remove_logs').get_item(
        Key={
            "object_name": bean.name,
            "deleted_at": bean.time
        },
    )
    print(response)
    assert response['Item']['object_name'] == bean.name
    assert response['Item']['deleted_at'] == bean.time

if __name__ == '__main__':
    test_write_log()
    test_write_ddb()
