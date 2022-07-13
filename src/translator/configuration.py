import os.path

from celestine.main import configuration


TRANSLATOR = "translator"
CONFIGURATION = "key.ini"

AZURE = "azure"
KEY = "key"
REGION = "region"
URL = "url"

key = ""  # secret
region = ""  # secret
url = "https://api.cognitive.microsofttranslator.com/translate"


def make(path):
    """A quick way to make a configuration file on disk."""
    configuration = configparser.ConfigParser()

    configuration.add_section(AZURE)
    configuration.set(AZURE, KEY, key)
    configuration.set(AZURE, REGION, region)
    configuration.set(AZURE, URL, url)

    save(path, configuration)


def load(directory):
    file = os.path.join(directory, TRANSLATOR, CONFIGURATION)
    return configuration.load(file)


class Translator():
    """A translator."""

    def __init__(self, directory):
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
