import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Specify subnet details
vpc_id = 'your_vpc_id'
cidr_block = '10.0.1.0/24'
availability_zone = 'us-east-1a'

# Create subnet
response = ec2.create_subnet(VpcId=vpc_id, CidrBlock=cidr_block, AvailabilityZone=availability_zone)

# Retrieve subnet ID
subnet_id = response['Subnet']['SubnetId']

print("Subnet created with ID:", subnet_id)
