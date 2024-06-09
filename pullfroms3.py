import boto3
import os
from cryptography.fernet import Fernet

def decrypt_file():
    # Initialize S3 client
    s3_client = boto3.client('s3')

    # Get the encrypted file from S3
    bucket_name = 'yourbucket'
    object_key = 'encrypted/raw/mytextfile.txt'
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    encrypted_file_content = response['Body'].read()

    # Load the secret key from the file
    with open('pathto\fernet_secret_key.txt', 'r') as f:
        secret_key = f.read().strip()


    print(secret_key)
    # Decrypt the file content
    decryption_key = Fernet(secret_key)
    decrypted_file_content = decryption_key.decrypt(encrypted_file_content)

    print(decrypted_file_content)
    # Save the decrypted file to S3
    with open('decrypted_file.txt', 'wb') as f:
        f.write(decrypted_file_content)


# Call the decrypt_file function
decrypt_file()