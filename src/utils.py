import boto3


def set_db_connection():

    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIA2JYPH33Q4KP3JE3Y',
        aws_secret_access_key='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'
    )

    return s3
