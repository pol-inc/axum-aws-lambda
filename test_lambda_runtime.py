import json
import requests


def mk_request(method="GET", body=None):
    return {
        "body": json.dumps(body) if body else "",
        "headers": {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Host": "localhost:5000",
            "User-Agent": "insomnia/2022.2.1",
        },
        "httpMethod": method,
        "isBase64Encoded": False,
        "multiValueHeaders": {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Host": "localhost:5000",
            "User-Agent": "insomnia/2022.2.1",
        },
        "path": "/",
        "queryStringParameters": {},
    }


requests.post(
    "http://localhost:9000/2015-03-31/functions/function/invocations",
    json=mk_request(method="POST", body={"name": "John Smith"}),
)
response = requests.post(
    "http://localhost:9000/2015-03-31/functions/function/invocations", json=mk_request()
).json()

print(json.dumps(json.loads(response["body"]), indent=2))
