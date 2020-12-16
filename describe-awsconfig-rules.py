import boto3
from botocore.exceptions import ClientError
import os


os.environ['AWS_PROFILE'] = "soc-master-admin"
os.environ['AWS_DEFAULT_REGION'] = "us-east-1"
config = boto3.client('config',region_name='us-east-1')

try:
    response = config.describe_config_rules()
    for rule in response['ConfigRules']:
        print('\n\r' + str(rule))
        print('\n\r' + str(rule))
except ClientError as e:
    print(e)

