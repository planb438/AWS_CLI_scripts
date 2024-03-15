import boto3

def create_eb_environment(application_name, environment_name, solution_stack_name, instance_type='t2.micro', database_name='mydatabase', db_username='admin', db_password='password'):
    """
    Create an Elastic Beanstalk environment with a LAMP stack.
    
    :param application_name: Name of the Elastic Beanstalk application.
    :param environment_name: Name of the environment to create.
    :param solution_stack_name: Solution stack name for LAMP environment.
    :param instance_type: EC2 instance type for the environment (default: t2.micro).
    :param database_name: Name of the MySQL database to create (default: mydatabase).
    :param db_username: Username for MySQL database (default: admin).
    :param db_password: Password for MySQL database (default: password).
    """
    client = boto3.client('elasticbeanstalk')

    # Create environment
    response = client.create_environment(
        ApplicationName=application_name,
        EnvironmentName=environment_name,
        SolutionStackName=solution_stack_name,
        OptionSettings=[
            {
                'Namespace': 'aws:autoscaling:launchconfiguration',
                'OptionName': 'InstanceType',
                'Value': instance_type
            },
            {
                'Namespace': 'aws:rds:dbinstance',
                'OptionName': 'DBDeletionPolicy',
                'Value': 'Delete'
            },
            {
                'Namespace': 'aws:rds:dbinstance',
                'OptionName': 'DBEngine',
                'Value': 'mysql'
            },
            {
                'Namespace': 'aws:rds:dbinstance',
                'OptionName': 'DBInstanceClass',
                'Value': 'db.t2.micro'
            },
            {
                'Namespace': 'aws:rds:dbinstance',
                'OptionName': 'DBName',
                'Value': database_name
            },
            {
                'Namespace': 'aws:rds:dbinstance',
                'OptionName': 'DBPassword',
                'Value': db_password
            },
            {
                'Namespace': 'aws:rds:dbinstance',
                'OptionName': 'DBUser',
                'Value': db_username
            }
        ]
    )

    print("Environment created successfully:", response['EnvironmentName'])

# Example usage
if __name__ == "__main__":
    create_eb_environment(
        application_name='my-application',
        environment_name='my-lamp-environment',
        solution_stack_name='64bit Amazon Linux 2 v3.4.0 running PHP 7.4'
    )
