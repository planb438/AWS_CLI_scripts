import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Create Internet Gateway
response = ec2.create_internet_gateway()

# Retrieve Internet Gateway ID
igw_id = response['InternetGateway']['InternetGatewayId']

print("Internet Gateway created with ID:", igw_id)
