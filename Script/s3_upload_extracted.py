import boto3

file_name = "data/source/extracted_allCategory.csv"
bucket = 'arxiv-bucket'
s3_client = boto3.client('s3')
try:
    response = s3_client.upload_file(file_name, bucket, 'source/extracted_allCategory.csv')
except ClientError as e:
    logging.error(e)
