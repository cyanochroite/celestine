"""Application for translating text to other languages."""
from celestine.main.configuration import configuration_load_main

from celestine.application.language.keyword import LANGUAGE

from celestine.application.language.keyword import KEY
from celestine.application.language.keyword import REGION
from celestine.application.language.keyword import URL


from celestine.application.language import configure


class Translator():
    """A translator."""

    def _attribute(self, default, configuration, name):
        attribute = default[LANGUAGE][name]

        if configuration.has_option(LANGUAGE, name):
            attribute = configuration[LANGUAGE][name]

        setattr(self, name, attribute)

    def __init__(self, path):
        self.key = None
        self.region = None
        self.url = None

        default = configure.default()

        configuration = configuration_load_main(path)

        self._attribute(default, configuration, KEY)
        self._attribute(default, configuration, REGION)
        self._attribute(default, configuration, URL)

    def endpoint(self):
        """Return the URL."""
        return self.url

    def header(self, trace):
        """Return the header."""
        return {
            "Ocp-Apim-Subscription-Key": self.key,
            "Ocp-Apim-Subscription-Region": self.region,
            "Content-type": "application/json",
            "X-ClientTraceId": trace,
        }

    def parameter(self, to_language):
        """Return the parameter."""
        return {
            "api-version": "3.0",
            "to": to_language,
            "category": "general",
            "from": "en",
            "includeAlignment": False,
            "includeSentenceLength": False,
            "profanityAction": "NoAction",
            "profanityMarker": "Asterisk",
            "suggestedFrom": "en",
            "textType": "plain",
        }
