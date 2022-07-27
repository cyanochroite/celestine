"""Application for translating text to other languages."""

from celestine.main.configuration import configuration_load


from celestine.keyword.main import CELESTINE


from celestine.application.language.keyword  import LANGUAGE

from celestine.application.language.keyword  import KEY
from celestine.application.language.keyword  import REGION
from celestine.application.language.keyword  import URL

from celestine.application.language.keyword  import FILE



from celestine.application.language.configure import configure


class Translator():
    """A translator."""

    def set_attribute(self, default, configuration, name):
        attribute = default[LANGUAGE][name]

        if configuration.has_option(LANGUAGE, name):
            attribute = configuration[LANGUAGE][name]

        setattr(self, name, attribute)

    def __init__(self, path):
        default = configure()

        configuration = configuration_load(
            path,
            CELESTINE,
            FILE
        )

        self.set_attribute(default, configuration, KEY)
        self.set_attribute(default, configuration, REGION)
        self.set_attribute(default, configuration, URL)

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

