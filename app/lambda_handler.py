import json

from app.src.configuration.DynamoDB_config import Dynamodb_Config
class lambda_handler:
    with open(file="./src/massa/evento.json") as file:
        event=json.load(file)
    def lambda_landler(event, context):
        print(f'Evento recebido: {event}')


    if __name__ == '__main__':
        Dynamodb_Config
        lambda_landler(event,None)