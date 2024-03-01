import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Specify instance IDs to start
instance_ids = ['instance_id_1', 'instance_id_2']

# Start EC2 instances
ec2.start_instances(InstanceIds=instance_ids)
