import boto3

def create_iam_user(username, policy_arn):
    iam = boto3.client('iam')
    
    # Create IAM user
    iam.create_user(UserName=username)
    
    # Attach policy to user
    iam.attach_user_policy(UserName=username, PolicyArn=policy_arn)
    
    print(f"IAM user '{username}' created successfully.")

if __name__ == "__main__":
    username = 'my-user'
    policy_arn = 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
    create_iam_user(username, policy_arn)
