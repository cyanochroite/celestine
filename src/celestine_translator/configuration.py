import configparser
import os.path

from celestine.main.configuration import configuration_load


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
    figtree = configparser.ConfigParser()

    figtree.add_section(AZURE)
    figtree.set(AZURE, KEY, key)
    figtree.set(AZURE, REGION, region)
    figtree.set(AZURE, URL, url)

    configuration.save(path, figtree)


def load(directory):
    file = os.path.join(directory, CONFIGURATION)
    return configuration_load(file)


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
