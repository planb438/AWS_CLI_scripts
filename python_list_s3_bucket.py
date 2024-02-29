import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Retrieve list of S3 buckets
response = s3.list_buckets()

# Print bucket names
for bucket in response['Buckets']:
    print("Bucket Name:", bucket['Name'])
