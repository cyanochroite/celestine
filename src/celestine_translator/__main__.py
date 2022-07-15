import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

import json
import requests
import uuid

from celestine_translator.configuration import Translator
from celestine_translator.configuration import *


path = os.path.join(directory, "key.ini")
make(path)


translator = Translator(directory)

TEXT = "text"

text = "I would really like to drive your car around the block a few times!"
text = "text"
text = "Fish in the sun is fun."


json = [
    {TEXT: text},
    {TEXT: "apple pie"}
]


from celestine.main import configuration

file = os.path.join(directory, "celestine_translator", "language.ini")
config = configuration.load(file)

config["application"]["title"] += "frenchy"
config["curses"]["exit"] += "language"

path = os.path.join(directory, "celestine", "language", "french.ini")
configuration.save(path, config)


def post(body):
    url = translator.url
    data = None
    json = body
    headers = {
        "Ocp-Apim-Subscription-Key": translator.key,
        "Ocp-Apim-Subscription-Region": translator.region,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4())
    }
    params = {
        "api-version": "3.0",
        "from": 'en',
        'includeSentenceLength': True,
        "to": [
            "fr",
            "de",
            "tlh-Latn",
            "tlh-Piqd",
        ]
    }
    return requests.post(url, data, json, headers=headers, params=params)


#request = post(json)
#response = request.json()

#candy = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))

print(response)
one = response[0]
two = response[1]["translations"]

print("MOO")
print(one)
print("MOO")
print(two)


