import boto3
from ..services import util

client = boto3.client('ec2')

def describe_tags(id):
    filter = {'Name': 'resource-id', 'Values': [id]}
    response = client.describe_tags(Filters=[filter])
    return response.get('Tags')

def _get_tag_value(tags, key):
    for tag in tags:
        if tag.get('Key') == key:
            return tag.get('Value')
