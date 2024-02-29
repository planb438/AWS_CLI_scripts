#!/bin/bash

# Set variables
DB_INSTANCE_IDENTIFIER="your_db_instance_identifier"
DB_INSTANCE_CLASS="your_db_instance_class"
ENGINE="your_database_engine"
MASTER_USERNAME="your_master_username"
MASTER_PASSWORD="your_master_password"

# Run AWS CLI command to create RDS instance
aws rds create-db-instance \
    --db-instance-identifier $DB_INSTANCE_IDENTIFIER \
    --db-instance-class $DB_INSTANCE_CLASS \
    --engine $ENGINE \
    --master-username $MASTER_USERNAME \
    --master-user-password $MASTER_PASSWORD
