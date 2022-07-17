import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

import json
import requests
import uuid
import configparser

from celestine_translator.translator import Translator

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_save

from celestine.main.keyword import language
from celestine.main.keyword import languages

TRANSLATIONS = "translations"
TEXT = "text"
TO = "to"

moose = {}

translator = Translator(directory)


def post(text):
    url = translator.endpoint()
    data = None
    json = [{TEXT: "apple pie"}]
    headers = translator.header(str(uuid.uuid4()))
    params = translator.parameter(["fr", "de", ])
    request = requests.post(url, data, json, headers=headers, params=params)
    return request.json()
    

print(post("Celestine Image Viewer"))
print("done")