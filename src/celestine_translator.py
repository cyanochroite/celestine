import sys



import requests
import uuid
import configparser


from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_save

from celestine.main.keyword import language
from celestine.main.keyword import languages


from celestine.keyword.translator import AZURE

from celestine.keyword.translator import KEY
from celestine.keyword.translator import REGION
from celestine.keyword.translator import URL

from celestine.keyword.translator import FILE


from celestine.keyword.translator import TRANSLATIONS
from celestine.keyword.translator import TEXT
from celestine.keyword.translator import TO



class Translator():
    """A translator."""

    def __init__(self, directory):
        self.configuration = configuration_load(directory, FILE)
        self.key = self.configuration[AZURE][KEY]
        self.region = self.configuration[AZURE][REGION]
        self.url = self.configuration[AZURE][URL]

    def endpoint(self):
        return translator.url

    def header(self, trace):
        return {
            "Ocp-Apim-Subscription-Key": self.key,
            "Ocp-Apim-Subscription-Region": self.region,
            "Content-type": "application/json",
            "X-ClientTraceId": trace,
        }

    def parameter(self, language):
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





directory = sys.path[0]



moose = {}

translator = Translator(directory)


def post(text):
    url = translator.endpoint()
    data = None
    json = [{TEXT: text}]
    headers = translator.header(str(uuid.uuid4()))
    params = translator.parameter(language)
    request = requests.post(url, data, json, headers=headers, params=params)
    return request.json()
    


def new_parser():
    for name in language:
        moose[name] = configparser.ConfigParser()


def add_section(section):
    for name in language:
        moose[name].add_section(section)


def add_item(section, key, value):
    items = post(value)
    for item in items:
        translations = item[TRANSLATIONS]
        for translation in translations:
            text = translation[TEXT]
            to = translation[TO]
            put = languages[to]
            name = put
            moose[name].set(section, key, text)


def save_item():
    for name in language:
        configuration_save(moose[name], directory, "celestine", "language", F"{name}.ini")


configuration = configuration_load(directory, "language.ini")
mydict = vars(configuration)["_sections"]

new_parser()
for section, dictionary in mydict.items():
    add_section(section)
    for key, value in dictionary.items():
        add_item(section, key, value)

save_item()


print(moose)
print("done")
