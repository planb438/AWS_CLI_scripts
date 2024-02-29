#!/bin/bash

# Set variables
REGION="your_region"
INSTANCE_TYPE="your_instance_type"
KEY_NAME="your_key_pair_name"
SECURITY_GROUP_ID="your_security_group_id"
SUBNET_ID="your_subnet_id"
IMAGE_ID="your_ami_id"

# Run AWS CLI command to create EC2 instance
aws ec2 run-instances \
    --region $REGION \
    --instance-type $INSTANCE_TYPE \
    --key-name $KEY_NAME \
    --security-group-ids $SECURITY_GROUP_ID \
    --subnet-id $SUBNET_ID \
    --image-id $IMAGE_ID
