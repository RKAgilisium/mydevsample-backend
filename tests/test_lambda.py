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
            ]
