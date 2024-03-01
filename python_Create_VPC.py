import boto3

# Create a VPC client
ec2 = boto3.client('ec2')

# Specify VPC details
cidr_block = '10.0.0.0/16'

# Create VPC
response = ec2.create_vpc(CidrBlock=cidr_block)

# Retrieve VPC ID
vpc_id = response['Vpc']['VpcId']

print("VPC created with ID:", vpc_id)
