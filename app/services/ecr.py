import boto3
from ..services import util

client = boto3.client('ecr')

def describe_repositories():
    response = client.describe_repositories()
    ret = {}
    for repo in response['repositories']:
        ret[repo['repositoryName']] = repo['repositoryArn']
        print(f"{repo['repositoryName']}\t{repo['repositoryArn']}")
    return ret
    