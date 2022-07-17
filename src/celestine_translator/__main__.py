import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

import json
import requests
import uuid

from celestine_translator.translator import Translator

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_save



translator = Translator(directory)

TEXT = "text"

text = "I would really like to drive your car around the block a few times!"
text = "text"
text = "Fish in the sun is fun."


json = [
    {TEXT: text},
    {TEXT: "apple pie"}
]


file = os.path.join(directory, "celestine_translator", "language.ini")
config = configuration_load(file)


def post(body):
    url = translator.endpoint()
    data = None
    json = body
    headers = translator.header(str(uuid.uuid4()))
    params = translator.parameter(["fr", "de", ])
    return requests.post(url, data, json, headers=headers, params=params)


request = post(json)
response = request.json()

#candy = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))

print(response)
one = response[0]
two = response[1]["translations"]

print("MOO")
print(one)
print("MOO")
print(two)


