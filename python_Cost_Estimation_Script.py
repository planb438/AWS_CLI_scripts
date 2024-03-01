import boto3

def estimate_cost():
    client = boto3.client('ce', region_name='us-east-1')
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': '2022-01-01',
            'End': '2022-01-31'
        },
        Granularity='MONTHLY',
        Metrics=['BlendedCost']
    )
    total_cost = response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']
    print(f"Estimated cost for January 2022: ${total_cost}")

if __name__ == "__main__":
    estimate_cost()
