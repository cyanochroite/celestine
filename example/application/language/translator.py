"""Application for translating text to other languages."""


class Translator():
    """A translator."""
    def __init__(self, attribute):
        self.key = attribute.key
        self.region = attribute.region
        self.url = attribute.url

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
