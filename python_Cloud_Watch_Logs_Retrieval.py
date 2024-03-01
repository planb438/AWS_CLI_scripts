import boto3

def retrieve_cloudwatch_logs(log_group_name, start_time, end_time):
    cloudwatch = boto3.client('logs')
    response = cloudwatch.get_log_events(
        logGroupName=log_group_name,
        startTime=start_time,
        endTime=end_time
    )
    for event in response['events']:
        print(event['message'])

if __name__ == "__main__":
    log_group_name = '/aws/lambda/my-function'
    start_time = 1645129200000  # Start time in milliseconds since epoch
    end_time = 1645132800000    # End time in milliseconds since epoch
    retrieve_cloudwatch_logs(log_group_name, start_time, end_time)
