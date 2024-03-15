import boto3

def create_copilot_service(app_name, svc_name, svc_type, svc_port, container_port, image):
    """
    Create an ECS service using AWS Copilot.
    
    :param app_name: Name of the Copilot application.
    :param svc_name: Name of the service to create.
    :param svc_type: Type of the service (e.g., 'Load Balanced Web Service').
    :param svc_port: Port on the host to bind to (e.g., 80).
    :param container_port: Port on the container to forward traffic to (e.g., 8080).
    :param image: Docker image to use for the service.
    """
    copilot = boto3.client('copilot')
    
    response = copilot.init(
        applicationName=app_name,
        serviceName=svc_name,
        serviceType=svc_type
    )

    # Override default service configuration
    svc_manifest = {
        "container": {
            "port": container_port,
            "image": image
        },
        "http": {
            "port": svc_port
        }
    }
    
    response = copilot.update(
        applicationName=app_name,
        serviceName=svc_name,
        manifest=svc_manifest
    )

    print("Copilot service created successfully:", svc_name)

# Example usage
if __name__ == "__main__":
    create_copilot_service(
        app_name='my-app',
        svc_name='my-service',
        svc_type='Load Balanced Web Service',
        svc_port=80,
        container_port=8080,
        image='my-ecr-repo/my-image:latest'
    )
