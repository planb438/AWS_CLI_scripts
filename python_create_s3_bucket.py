import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Specify bucket name
bucket_name = 'your_bucket_name'

# Create S3 bucket
s3.create_bucket(Bucket=bucket_name)
