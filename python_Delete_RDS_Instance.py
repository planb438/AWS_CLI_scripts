import boto3

# Create an RDS client
rds = boto3.client('rds')

# Specify RDS instance identifier to delete
db_instance_identifier = 'your_db_instance_identifier'

# Delete RDS instance
rds.delete_db_instance(DBInstanceIdentifier=db_instance_identifier, SkipFinalSnapshot=True)
