import boto3
import json
import pytest
import re

def setup():
    f = open('./output.json')
    data = json.load(f)
    arns = []
    
    for key, value in data['cdktf-project'].items():
        if value.startswith('arn:'):
            arns.append(value)
    
    return arns

def test():
    arns = setup()

    for arn in arns:
        if re.search('s3', arn):
            resource_name = arn.split(":")[-1]
            client = boto3.client('s3')
            response = client.head_bucket(
                Bucket=resource_name
            )

            assert response['ResponseMetadata']['HTTPStatusCode'] == 200

