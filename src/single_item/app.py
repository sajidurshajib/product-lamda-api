import boto3
import os
import json
import uuid
from datetime import datetime


def lambda_handler(message, context):

    if ('body' not in message or message['httpMethod'] != 'GET'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }

    table_name = os.environ.get('TABLE', 'Items')
    region = os.environ.get('REGION', 'us-east-1')

    item_table = boto3.resource(
        'dynamodb',
        region_name=region
    )

    table = item_table.Table(table_name)
    # activity = json.loads(message['body'])
    item_id = message['pathParameters']['id']

    params = {
        'id': item_id
    }

    response = table.get_item(Key=params)

    print(response)

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Item'])
    }
