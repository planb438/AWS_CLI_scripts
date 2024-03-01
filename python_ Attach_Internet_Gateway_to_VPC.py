import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Specify VPC and Internet Gateway IDs
vpc_id = 'your_vpc_id'
igw_id = 'your_igw_id'

# Attach Internet Gateway to VPC
ec2.attach_internet_gateway(VpcId=vpc_id, InternetGatewayId=igw_id)

print("Internet Gateway attached to VPC:", vpc_id)
