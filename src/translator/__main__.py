import os.path
import sys

directory = sys.path[0] = os.path.dirname(sys.path[0])
sys.path.append(directory)

import json
import requests
import uuid

from translator.configuration import Translator


translator = Translator(directory)

text = "I would really like to drive your car around the block a few times!"

params = {
    "api-version": "3.0",
    "from": 'en',
    'includeSentenceLength': True,
    "to": [
        "fr",
        "zu"
    ]
}

headers = {
    "Ocp-Apim-Subscription-Key": translator.key,
    "Ocp-Apim-Subscription-Region": translator.region,
    "Content-type": 'application/json',
    "X-ClientTraceId": str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    "text": text
}]

request = requests.post(translator.url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
