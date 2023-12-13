import boto3


def set_db_connection():

    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIA2JYPH33QU6WTSDR5',
        aws_secret_access_key='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'
    )

    return s3
