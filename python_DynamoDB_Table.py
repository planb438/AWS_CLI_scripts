import boto3

def create_dynamodb_table(table_name, key_schema, attribute_definitions, provisioned_throughput):
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput
    )
    print(f"DynamoDB table '{table_name}' created successfully.")

if __name__ == "__main__":
    table_name = 'my-table'
    key_schema = [
        {'AttributeName': 'id', 'KeyType': 'HASH'},
        {'AttributeName': 'timestamp', 'KeyType': 'RANGE'}
    ]
    attribute_definitions = [
        {'AttributeName': 'id', 'AttributeType': 'S'},
        {'AttributeName': 'timestamp', 'AttributeType': 'N'}
    ]
    provisioned_throughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
    create_dynamodb_table(table_name, key_schema, attribute_definitions, provisioned_throughput)
