import boto3

def deploy_to_elastic_beanstalk(application_name, environment_name, version_label, source_bundle):
    client = boto3.client('elasticbeanstalk')
    response = client.create_application_version(
        ApplicationName=application_name,
        VersionLabel=version_label,
        SourceBundle=source_bundle
    )
    response = client.update_environment(
        ApplicationName=application_name,
        EnvironmentName=environment_name,
        VersionLabel=version_label
    )
    print(f"Application deployed to Elastic Beanstalk environment '{environment_name}'.")

if __name__ == "__main__":
    application_name = 'my-application'
    environment_name = 'my-environment'
    version_label = 'v1.0'
    source_bundle = {'S3Bucket': 'my-bucket', 'S3Key': 'app.zip'}
    deploy_to_elastic_beanstalk(application_name, environment_name, version_label, source_bundle)
