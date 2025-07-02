import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    lead_id = event['body']['lead_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('leads')
    response = table.query(
        KeyConditionExpression=Key('lead_id').eq(lead_id)
    )
    items = response['Items']
    # Salida (json)
    return {
        'statusCode': 200,
        'response': items
    }
