import boto3

def create_auto_scaling_group(group_name, launch_template_id, min_size, max_size, desired_capacity):
    client = boto3.client('autoscaling')
    response = client.create_auto_scaling_group(
        AutoScalingGroupName=group_name,
        LaunchTemplate={
            'LaunchTemplateId': launch_template_id,
            'Version': '$Latest'
        },
        MinSize=min_size,
        MaxSize=max_size,
        DesiredCapacity=desired_capacity
    )
    print(f"Auto Scaling Group '{group_name}' created successfully.")

if __name__ == "__main__":
    group_name = 'my-asg'
    launch_template_id = 'lt-1234567890abcdef0'
    min_size = 1
    max_size = 5
    desired_capacity = 2
    create_auto_scaling_group(group_name, launch_template_id, min_size, max_size, desired_capacity)
