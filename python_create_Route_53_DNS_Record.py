import boto3

def create_dns_record(zone_id, name, value, record_type):
    route53 = boto3.client('route53')
    response = route53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': name,
                        'Type': record_type,
                        'TTL': 300,
                        'ResourceRecords': [
                            {
                                'Value': value
                            }
                        ]
                    }
                }
            ]
        }
    )
    print(f"DNS record '{name}' created successfully.")

if __name__ == "__main__":
    zone_id = 'Z1234567890ABCDEF'
    name = 'example.com'
    value = '192.0.2.1'
    record_type = 'A'
    create_dns_record(zone_id, name, value, record_type)
