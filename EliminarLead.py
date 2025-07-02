import boto3

def lambda_handler(event, context):
    # Entrada (json)
    lead_id = event['body']['lead_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('leads')
    response = table.delete_item(
        Key={
            'lead_id': lead_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
