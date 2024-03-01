import boto3

# Create a CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Specify alarm details
alarm_name = 'your_alarm_name'
metric_name = 'your_metric_name'
namespace = 'AWS/EC2'
statistic = 'Average'
threshold = 80.0
comparison_operator = 'GreaterThanThreshold'
evaluation_periods = 1
period = 300
alarm_actions = ['arn:aws:sns:us-east-1:123456789012:your-sns-topic']

# Create CloudWatch alarm
cloudwatch.put_metric_alarm(
    AlarmName=alarm_name,
    MetricName=metric_name,
    Namespace=namespace,
    Statistic=statistic,
    Threshold=threshold,
    ComparisonOperator=comparison_operator,
    EvaluationPeriods=evaluation_periods,
    Period=period,
    AlarmActions=alarm_actions
)
