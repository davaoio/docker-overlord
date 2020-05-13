import boto3
from ..services import util

client = boto3.client('ecr')

def describe_repositories():
    response = client.describe_repositories()
    return response.get('repositories')

def describe_images(repositoryName):
    response = client.describe_images(repositoryName=repositoryName)
    return response.get('imageDetails')
