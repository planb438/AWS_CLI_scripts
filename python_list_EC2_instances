import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Retrieve list of EC2 instances
response = ec2.describe_instances()

# Print instance details
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID:", instance['InstanceId'])
        print("Instance Type:", instance['InstanceType'])
        print("Public DNS:", instance['PublicDnsName'])
        print("State:", instance['State']['Name'])
        print("----------------------")
