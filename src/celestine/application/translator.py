"""Application for translating text to other languages."""
import uuid
import requests
import os.path
import shutil
import keyword

from celestine.main.configuration import configuration_load

from celestine.keyword.main import code
from celestine.keyword.main import language
from celestine.keyword.main import languages
from celestine.keyword.main import WRITE
from celestine.keyword.main import UTF_8


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


class Window():
    def __init__(self, session):
        self.session = session

    def file_dialog(self, tag, bind):
        pass

    def file_dialog_load(self, tag):
        pass

    def image(self, tag, image):
        pass

    def image_load(self, file):
        pass

    def label(self, tag, text):
        pass

    def reset(self):
        path = os.path.join(self.directory, "celestine", "language")
        if os.path.islink(path):
            raise RuntimeError

        if os.path.isdir(path):
            shutil.rmtree.avoids_symlink_attacks
            shutil.rmtree(path, ignore_errors=False, onerror=None)

        os.mkdir(path)

    def header(self):
        path = os.path.join(self.directory, "celestine", "language", "__init__.py")
        with open(path, WRITE, encoding=UTF_8) as file:
            file.write(F'"""Lookup table for languages."""\n')

    def format_line(self, item):
        (name, value) = item
        if not name.isidentifier():
            raise ValueError("Not a valid identifier.")
        if keyword.iskeyword(name) or keyword.issoftkeyword(name):
            raise ValueError("This work is a keyword.")
        value = value.replace('"', "'")
        return F'{name} = "{value}"\n'

    def post(self, text):
        """Generate a post request."""
        url = self.translator.endpoint()
        data = None
        json = [{TEXT: text}]
        headers = self.translator.header(str(uuid.uuid4()))
        params = self.translator.parameter(code)
        request = requests.post(url, data, json, headers=headers, params=params)
        return request.json()

    def add_item(self, key, value):
        """Add item to parsers."""
        items = self.post(value)
        for item in items:
            translations = item[TRANSLATIONS]
            for translation in translations:
                text = translation[TEXT]
                put = languages[translation[TO]]
                name = put
                self.moose[name].append((key, text))

    def save_item(self):
        """Save the items."""
        for name in language:
            path = os.path.join(self.directory, "celestine", "language", F"{name}.py")
            items = self.moose[name]
            with open(path, WRITE, encoding=UTF_8) as file:
                file.write(F'"""Lookup table for {name}."""\n')
                file.writelines(map(self.format_line, items))

    def parser_magic(self):
        """Do all parser stuff here."""
        for name in language:
            self.moose[name] = []

        for name, value in thelist.items():
            self.add_item(name, value)

    def run(self, app):
        self.moose = {}
        self.directory = app.session.directory
        self.translator = Translator(app.session.directory)

        self.parser_magic()

        self.reset()
        self.header()
        self.save_item()

        print(self.moose)
        print("done")



