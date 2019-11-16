

def handler(event, context):
    print(event['queryStringParameters'])
    query = event['queryStringParameters']['q']
