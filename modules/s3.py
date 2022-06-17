import boto3
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def get_files():
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-2',
        aws_access_key_id=os.getenv('KEY_ID'),
        aws_secret_access_key=os.getenv('SECRET')
    )

    for obj in s3.Bucket('vinhtestbucket2').objects.all():
        print(obj.key)

    obj = s3.Bucket('vinhtestbucket2').Object('reviewTest.csv').get()
    foo = pd.read_csv(obj['Body'])
    bar = pd.DataFrame(foo).fillna('NULL')
    return bar

