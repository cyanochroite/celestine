import configparser
import os.path

from celestine.main.configuration import configuration_load

from celestine_translator.keyword import AZURE

from celestine_translator.keyword import KEY
from celestine_translator.keyword import REGION
from celestine_translator.keyword import URL

from celestine_translator.keyword import FILE


class Translator():
    """A translator."""

    def __init__(self, directory):
        self.configuration = configuration_load(directory, FILE)
        self.key = self.configuration[AZURE][KEY]
        self.region = self.configuration[AZURE][KEY]
        self.url = self.configuration[AZURE][KEY]

    def endpoint():
        return "https://api.cognitive.microsofttranslator.com/translate"

    def header(trace):
        return {
            "Ocp-Apim-Subscription-Key": self.key,
            "Ocp-Apim-Subscription-Region": self.region,
            "Content-type": "application/json",
            "X-ClientTraceId": trace,
        }

    def parameter(language):
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
