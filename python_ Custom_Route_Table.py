import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Specify VPC ID
vpc_id = 'your_vpc_id'

# Create Route Table
response = ec2.create_route_table(VpcId=vpc_id)

# Retrieve Route Table ID
route_table_id = response['RouteTable']['RouteTableId']

print("Route Table created with ID:", route_table_id)
