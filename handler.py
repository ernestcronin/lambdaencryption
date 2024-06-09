import json
import boto3
from cryptography.fernet import Fernet
import os

secret_key = os.environ['SECRET_KEY']

def encrypt_file(event, context):

 try:
       # Replace 'YOUR_SECRET_KEY' with your actual secret key
       #secret_key = Fernet.generate_key()
       print(secret_key)
       
       s3_client = boto3.client('s3')
       encryption_key = Fernet(secret_key)

       # Trigger the function on S3 bucket event
       bucket_name = event['Records'][0]['s3']['bucket']['name']
       object_key = event['Records'][0]['s3']['object']['key']
       print('Bucket name: ' + bucket_name);
       print('Object key: ' + object_key);

       # Check if the object is already encrypted
       if(object_key.startswith('encrypted/')):
          return 'Object is already encrypted';
      
       # Read the object from S3
       response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
       file_content = response['Body'].read()

       # Encrypt the file content
       encrypted_content = encryption_key.encrypt(file_content)

       # Upload the encrypted file back to S3
       s3_client.put_object(Bucket=bucket_name, Key='encrypted/' + object_key, Body=encrypted_content)
       
       print(f"File {object_key} encrypted and uploaded successfully.")
       
       return "Encryption successful!"
    
 except Exception as e:
       print(f"Error: {e}")
       return f"Error: {e}"