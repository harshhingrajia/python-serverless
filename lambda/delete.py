#!/usr/bin/env python
import boto3 
import json
import datetime

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

def delete(event, context):
    req_data = event['data']

    secret_key='...'
    access_key='...'
    region='...'
    user_pool_id='...'  
    
    if 'SECRET_KEY' in req_data:
        secret_key = req_data['SECRET_KEY']
    if 'ACCESS_KEY' in req_data:
        access_key = req_data['ACCESS_KEY']
    if 'REGION' in req_data:
        region = req_data['REGION']
    if 'USER_POOL_ID' in req_data:
        user_pool_id = req_data['USER_POOL_ID']

    client = boto3.client('cognito-idp', **{'aws_access_key_id': access_key, 'aws_secret_access_key': secret_key,\
     'region_name': region})
    
    bulk = req_data['Users']

    for username in bulk:
        bulk_delete = username['Username']
        response = client.admin_delete_user(
            UserPoolId=user_pool_id,    
            Username=bulk_delete
        )
        #json dump for date and time
        deleteusers = json.dumps(response, indent = 1, sort_keys=True,default=default)

    return json.loads(deleteusers)