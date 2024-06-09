<!--
title: 'encrypt a file on s3 with lambda function'
description: 'This template demonstrates how to deploy a Python function running on AWS Lambda using the traditional Serverless Framework.'
layout: Doc
framework: v3
platform: AWS
language: python
priority: 2
authorLink: '(https://github.com/ernestcronin)'
authorName: 'ecronin'
-->


# Serverless Framework AWS Python Example

Push a file to s3 using the python script pushtos3.py. Given the lambda function has been deployed, the file will be encrypted and stored under directory /encrypt. Be sure to add your secret key the lambda environment variable as SECRET_KEY=YOUR_KEY.
There is a seperate script called pullfroms3.py that will retrieve the file and decrypt the message.


### Deployment

In order to deploy the example, you need to run the following command:

```
$ serverless plugin install -n serverless-python-requirements - to download node modules
$ pip install on any missing dependencies

Update the bucket name, file name, aws profile, and path to your access/secret key in the files. You will also need to add the file to your Fernet Crypto key.

$ serverless deploy
```

After running deploy, you should see output similar to:

```bash
Deploying aws-python-project to stage dev (us-east-1)

✔ Service deployed to stack 

functions:
  encrypt_file: fileencrypter-dev-encrypt_file (1.5 kB)
```

### Invocation

run the script pushtos3.py. be sure to put the bucketname, filename and location of your was access/secret key. This will be in json format. 
{
  'access_key':key,
   'secret_key': key
 }
The file will be uploaded to the s3 bucket under folder encrypted. Be sure to look at CloudWatch logs for any issues.

run the script pullfroms3.py.
Be sure to add your bucket name, file name, and path to your fernet secret key. This should match the path in serverless.yml and the value in the Lambda function configuration.
```
