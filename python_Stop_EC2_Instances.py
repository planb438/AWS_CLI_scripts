import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Specify instance IDs to stop
instance_ids = ['instance_id_1', 'instance_id_2']

# Stop EC2 instances
ec2.stop_instances(InstanceIds=instance_ids)
