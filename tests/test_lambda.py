from moto import mock_dynamodb2
import pytest
import boto3
import os
from code import app

os.environ['tablename'] = 'test'

@pytest.fixture
def use_moto():
    @mock_dynamodb2
    def dynamodb_client():
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        # Create the table
        dynamodb.create_table(
            TableName='test',
            KeySchema=[
                {
                    'AttributeName': 'Id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'Id',
                    'AttributeType': 'S'
                }
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        return dynamodb
    return dynamodb_client

@mock_dynamodb2
def test_handler_for_failure(use_moto):
    use_moto()
    event = {
        "id": "test"
    }

    return_data = app.lambda_handler(event, "")
    assert return_data['statusCode'] == 500
