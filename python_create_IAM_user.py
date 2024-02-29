import boto3

# Create an IAM client
iam = boto3.client('iam')

# Specify IAM user name
user_name = 'your_user_name'

# Create IAM user
iam.create_user(UserName=user_name)
