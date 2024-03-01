import boto3

def publish_to_sns_topic(topic_arn, message):
    sns = boto3.client('sns')
    sns.publish(
        TopicArn=topic_arn,
        Message=message
    )
    print("Message published to SNS topic.")

if __name__ == "__main__":
    topic_arn = 'arn:aws:sns:us-east-1:123456789012:my-topic'
    message = 'Hello from Python!'
    publish_to_sns_topic(topic_arn, message)
