import boto3

def create_rds_snapshot(db_instance_identifier, snapshot_identifier):
    client = boto3.client('rds')
    response = client.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_identifier,
        DBInstanceIdentifier=db_instance_identifier
    )
    print(f"Snapshot '{snapshot_identifier}' created successfully.")

if __name__ == "__main__":
    db_instance_identifier = 'my-db-instance'
    snapshot_identifier = 'my-snapshot'
    create_rds_snapshot(db_instance_identifier, snapshot_identifier)
