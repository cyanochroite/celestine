import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

import json
import requests
import uuid

from celestine_translator.configuration import Translator
from celestine_translator.configuration import *

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_save


#path = os.path.join(directory, "key.ini")
# make(path)


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
config = configuration_load(file)

def azure_endpoint():
    return "https://api.cognitive.microsofttranslator.com/translate"


def azure_header(key, region, trace):
    return {
        "Ocp-Apim-Subscription-Key": key,
        "Ocp-Apim-Subscription-Region": region,
        "Content-type": "application/json",
        "X-ClientTraceId": trace
    }


def azure_parameter(language):
    return {
        "api-version": "3.0",
        "to": language,
        "category": "general",
        "from": "en",
        "includeAlignment": False,
        "includeSentenceLength": False,
        "profanityAction": "NoAction",
        "profanityMarker": "Asterisk",
        "suggestedFrom": "en",
        "textType": "plain",
    }


def post(body):
    url = azure_endpoint()
    data = None
    json = body
    headers = azure_header(translator.key, translator.region, str(uuid.uuid4()))
    params = azure_parameter(["fr", "de", ])
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


