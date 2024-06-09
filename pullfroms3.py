import boto3
import os
from cryptography.fernet import Fernet

def decrypt_file():
    # Initialize S3 client
    s3_client = boto3.client('s3')
    print('in method')
    # Get the encrypted file from S3
    bucket_name = YOUR_BUCKET
    object_key = 'encrypted/raw/'+YOUR_FILE
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    encrypted_file_content = response['Body'].read()

    # Get the secret key from environment variable
    secret_key = os.environ['SECRET_KEY']
    print(secret_key)
    # Decrypt the file content
    decryption_key = Fernet(secret_key)
    decrypted_file_content = decryption_key.decrypt(encrypted_file_content)

    print(decrypted_file_content)
    # Save the decrypted file to S3
    with open('decrypted_file.txt', 'wb') as f:
        f.write(decrypted_file_content)


# Set the SECRET_KEY environment variable. Here is a sample key
os.environ['SECRET_KEY'] = 'q-wTFiX0GmnmSxyUsGb9PYpYmELGD1jS5heQYsNLFIE='

# Call the decrypt_file function
decrypt_file()