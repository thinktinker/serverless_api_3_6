import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Martin Leong created a function in serverless executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
