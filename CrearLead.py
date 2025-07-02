import boto3

def lambda_handler(event, context):
    # Entrada (json)
    lead = event['body']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('leads')
    response = table.put_item(Item=lead)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
