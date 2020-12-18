import json
import os
import boto3
from botocore.exceptions import ClientError
# import requests

def lambda_handler(event, context):
    """Sample pure Lambda function
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format
        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict
        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)
    #     raise e

    #session = boto3.Session(aws_access_key_id='read from ENV',aws_secret_access_key='REad from Env')
    #config = session.client('config',region_name='us-east-1')

    """ When running provide your profile name like this commnad >> sam local invoke -e .\events\event.json --profile aws-profilename-admin """
    config = boto3.client('config')
    try:
        response = config.describe_config_rules()
        fails = config.__module__.
        for rule in response['ConfigRules']:
            print("***********************************************")            
            print(rule,'   \n')
    except ClientError as e:
        print(e)


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world *******************",
            # "location": ip.text.replace("\n", "")
        }),
    }