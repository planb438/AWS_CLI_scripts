import boto3

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("S3 Buckets:")
    for bucket in buckets:
        print(bucket)

if __name__ == "__main__":
    list_s3_buckets()
