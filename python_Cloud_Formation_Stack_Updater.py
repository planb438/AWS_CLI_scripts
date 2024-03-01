import boto3

def update_cloudformation_stack(stack_name, template_url, parameters):
    client = boto3.client('cloudformation')
    response = client.update_stack(
        StackName=stack_name,
        TemplateURL=template_url,
        Parameters=parameters,
        Capabilities=['CAPABILITY_NAMED_IAM']
    )
    print(f"CloudFormation stack '{stack_name}' updated successfully.")

if __name__ == "__main__":
    stack_name = 'my-stack'
    template_url = 'https://s3.amazonaws.com/my-bucket/my-template.json'
    parameters = [
        {'ParameterKey': 'InstanceType', 'ParameterValue': 't2.micro'},
        {'ParameterKey': 'KeyName', 'ParameterValue': 'my-keypair'}
    ]
    update_cloudformation_stack(stack_name, template_url, parameters)
