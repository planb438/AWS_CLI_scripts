import boto3

def send_message_to_sqs_queue(queue_url, message_body):
    sqs = boto3.client('sqs')
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    print("Message sent to SQS queue.")

if __name__ == "__main__":
    queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/my-queue'
    message_body = 'Hello from Python!'
    send_message_to_sqs_queue(queue_url, message_body)
