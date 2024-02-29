#!/bin/bash

# Set variables
FUNCTION_NAME="your_function_name"
HANDLER="your_handler_function"
ROLE_ARN="your_execution_role_arn"
RUNTIME="your_runtime"
ZIP_FILE="your_function_code.zip"

# Create Lambda function
aws lambda create-function \
    --function-name $FUNCTION_NAME \
    --handler $HANDLER \
    --role $ROLE_ARN \
    --runtime $RUNTIME \
    --zip-file fileb://$ZIP_FILE
