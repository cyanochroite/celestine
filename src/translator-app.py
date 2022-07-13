import json
import requests
import uuid


key = ""
region = ""


endpoint = "https://api.cognitive.microsofttranslator.com"
# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.

path = "/translate"
constructed_url = endpoint + path

params = {
    "api-version": "3.0",
    "from": 'en',
    "to": [
        "fr",
        "zu"
    ]
}

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Ocp-Apim-Subscription-Region": region,
    "Content-type": 'application/json',
    "X-ClientTraceId": str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'I would really like to drive your car around the block a few times!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
