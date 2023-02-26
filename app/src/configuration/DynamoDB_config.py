import os

import boto3


# Configuração DynamoDB
class Dynamodb_Config:
    # Ambiente local
    if os.environ.get("ENVIRONMENT")== "local":
        print("Você esta e, ambiente local")
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")
