import boto3

def terminate_ec2_instance(instance_id):
    ec2 = boto3.client('ec2')
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"EC2 instance {instance_id} terminated successfully.")

if __name__ == "__main__":
    instance_id = 'i-1234567890abcdef0'
    terminate_ec2_instance(instance_id)
