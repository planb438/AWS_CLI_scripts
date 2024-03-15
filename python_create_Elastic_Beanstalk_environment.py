import boto3

def create_eb_environment(application_name, environment_name, solution_stack_name):
    """
    Create an Elastic Beanstalk environment.
    
    :param application_name: Name of the Elastic Beanstalk application.
    :param environment_name: Name of the environment to create.
    :param solution_stack_name: Solution stack name (e.g., "64bit Amazon Linux 2 v3.4.0 running Python 3.8").
    """
    client = boto3.client('elasticbeanstalk')

    response = client.create_environment(
        ApplicationName=application_name,
        EnvironmentName=environment_name,
        SolutionStackName=solution_stack_name
        # Additional parameters can be specified as needed
        # For example, you can specify the instance type, key name, security groups, etc.
    )

    print("Environment created successfully:", response['EnvironmentName'])

# Example usage
if __name__ == "__main__":
    create_eb_environment(
        application_name='my-application',
        environment_name='my-environment',
        solution_stack_name='64bit Amazon Linux 2 v3.4.0 running Python 3.8'
    )
