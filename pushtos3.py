import boto3
import json

BUCKET_NAME = YOUR_BUCKET
FILE_PATH = YOUR_FILE

# Read AWS credentials from a file
with open('YOUR_AWS_KEY_LOCATION', 'r') as f:
    aws_credentials = json.load(f)

ACCESS_KEY = aws_credentials['access_key']
SECRET_KEY = aws_credentials['secret_key']

# Create a S3 client using AWS credentials
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

try:
    # Upload the file to the specified S3 bucket
    object_key = 'raw/' + FILE_PATH.split('/')[-1]
    response = s3.upload_file(FILE_PATH, BUCKET_NAME, object_key)
    print("File uploaded successfully:", response)
except Exception as e:
    print("Error uploading file:", e)

