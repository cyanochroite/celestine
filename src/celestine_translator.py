"""Application for translating text to other languages."""
import sys
import uuid
import configparser
import requests


from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_save

from celestine.keyword.main import code
from celestine.keyword.main import language
from celestine.keyword.main import languages


from celestine.keyword.main import CONFIGURATION
from celestine.keyword.main import CELESTINE


from celestine.keyword.translator import AZURE

from celestine.keyword.translator import KEY
from celestine.keyword.translator import REGION
from celestine.keyword.translator import URL

from celestine.keyword.translator import FILE


from celestine.keyword.translator import TRANSLATIONS
from celestine.keyword.translator import TEXT
from celestine.keyword.translator import TO
from celestine.keyword.language import thelist

from celestine.main.configuration import configuration_translator


class Translator():
    """A translator."""

    def set_attribute(self, default, configuration, name):
        attribute = default[AZURE][name]

        if configuration.has_option(AZURE, name):
            attribute = configuration[AZURE][name]

        setattr(self, name, attribute)
    
    def __init__(self, path):
        default = configuration_translator("fish", "are", "friends")

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
        return translator.url

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

def reset():
    path = os.path.join(directory, "celestine", "language")
    if os.path.islink(path):
        raise RuntimeError
    
    if os.path.isdir(path):
        shutil.rmtree.avoids_symlink_attacks
        shutil.rmtree(path, ignore_errors=False, onerror=None)
    
    os.mkdir(path)
    
    
def header():
    path = os.path.join(directory, "celestine", "language", "__init__.py")
    with open(path, WRITE) as file:
        file.write(F'"""Lookup table for languages."""\n')



directory = sys.path[0]


moose = {}

translator = Translator(directory)

def format_line(item):
    (name, value) = item
    if not name.isidentifier():
        raise ValueError("Not a valid identifier.")
    if keyword.iskeyword(name) or keyword.issoftkeyword(name):
        raise ValueError("This work is a keyword.")
    value = value.replace('"', "'")
    return F'{name} = "{value}"\n'


def new_save(language):
    path = os.path.join(directory, "celestine", "language", F"{language}.py")
    items = moose[language]

    names = ['sugar', 'spice', 'everything_nice']
    values = ["1", "2", "3"]
    with open(path, WRITE) as file:
        file.write(F'"""Lookup table for {language}."""\n')
        file.writelines(map(format_line, names, values))


def post(text):
    """Generate a post request."""
    url = translator.endpoint()
    data = None
    json = [{TEXT: text}]
    headers = translator.header(str(uuid.uuid4()))
    params = translator.parameter(code)
    request = requests.post(url, data, json, headers=headers, params=params)
    return request.json()


def add_item(key, value):
    """Add item to parsers."""
    items = post(value)
    for item in items:
        translations = item[TRANSLATIONS]
        for translation in translations:
            text = translation[TEXT]
            put = languages[translation[TO]]
            name = put
            moose[name].append((key, text))


def save_item():
    """Save the items."""
    for name in language:
        path = os.path.join(directory, "celestine", "language", F"{name}.py")
        items = moose[name]
        with open(path, WRITE) as file:
            file.write(F'"""Lookup table for {name}."""\n')
            file.writelines(map(format_line, items))



def parser_magic():
    """Do all parser stuff here."""
    for name in language:
        moose[name] = []
    
    for item in thelist:
        (name, value) = item
        add_item(name, value)

    save_item()


reset()
header()

parser_magic()

print(moose)
print("done")
