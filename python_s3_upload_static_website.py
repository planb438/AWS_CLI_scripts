import boto3
import os

def create_s3_bucket(bucket_name):
    # Create S3 client
    s3_client = boto3.client('s3')

    # Create S3 bucket
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"S3 bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")

def upload_website_files(bucket_name, website_dir):
    # Create S3 resource
    s3_resource = boto3.resource('s3')

    # Upload website files
    for root, dirs, files in os.walk(website_dir):
        for file in files:
            file_path = os.path.join(root, file)
            key = os.path.relpath(file_path, website_dir)
            s3_resource.meta.client.upload_file(file_path, bucket_name, key)
            print(f"Uploaded {key} to S3 bucket.")

def configure_static_website(bucket_name):
    # Configure static website hosting
    s3_client = boto3.client('s3')
    try:
        s3_client.put_bucket_website(
            Bucket=bucket_name,
            WebsiteConfiguration={
                'IndexDocument': {'Suffix': 'index.html'}
            }
        )
        print("Static website hosting configured successfully.")
    except Exception as e:
        print(f"Error configuring static website hosting: {e}")

if __name__ == "__main__":
    # Bucket and website directory details
    bucket_name = 'your-bucket-name'
    website_dir = '/path/to/your/website/directory'

    # Create S3 bucket
    create_s3_bucket(bucket_name)

    # Upload website files to S3 bucket
    upload_website_files(bucket_name, website_dir)

    # Configure static website hosting
    configure_static_website(bucket_name)
