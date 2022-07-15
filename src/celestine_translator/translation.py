

TRANSLATIONS = "translations"
TEXT = "text"
TO = "to"

FR = "fr"
DE = "de"

FRANCE = "france"
GERMAN = "german"

class Translation():
    """A translator."""

    def __init__(self, response):
        two = response[TRANSLATIONS]
        self.configuration = load(directory)

    @property
    def key(self):
        """Returns the key."""
        return self.configuration[AZURE][KEY]

    @property
    def region(self):
        """Returns the region."""
        return self.configuration[AZURE][REGION]

    @property
    def url(self):
        """Returns the url."""
        return self.configuration[AZURE][URL]

moose = {}


configuration = configparser.ConfigParser()

configuration.add_section(APPLICATION)
configuration.set(APPLICATION, LANGUAGE, ENGLISH)
configuration.set(APPLICATION, PACKAGE, CELESTINE)
configuration.set(APPLICATION, PYTHON, PYTHON_3_10)
languages = {
    FR : FRANCE,
    DE : GERMAN,
}

figtree = {
    FRANCE : [],
    GERMAN : [],
}

figtree[language[0]]

def stuff(items):
    for item in items:
        translations = item[TRANSLATIONS]
        for translation in translations:
            text = translation[TEXT]
            to = translation[TO]
            language = languages[to]
            figtree[language].append(text)

print(response)
one = response[0]
two = response[1]["translations"]

[{'translations': [{'text': 'SMS', 'to': 'fr', 'sentLen': {'srcSentLen': [4], 'transSentLen': [3]}}, {'text': 'umbhalo', 'to': 'zu', 'sentLen': {'srcSentLen': [4], 'transSentLen': [7]}}]}, {'translations': [{'text': 'tarte aux pommes', 'to': 'fr', 'sentLen': {'srcSentLen': [9], 'transSentLen': [16]}}, {'text': 'i - a pie', 'to': 'zu', 'sentLen': {'srcSentLen': [9], 'transSentLen': [9]}}]}]
[
    {'translations': [
        {'text': 'SMS', 'to': 'fr', 'sentLen': {'srcSentLen': [4], 'transSentLen': [3]}},
        {'text': 'umbhalo', 'to': 'zu', 'sentLen': {'srcSentLen': [4], 'transSentLen': [7]}}
        ]
     },
    {'translations': [
        {'text': 'tarte aux pommes', 'to': 'fr', 'sentLen': {'srcSentLen': [9], 'transSentLen': [16]}},
        {'text': 'i - a pie', 'to': 'zu', 'sentLen': {'srcSentLen': [9], 'transSentLen': [9]}}
    ]
     }
]
