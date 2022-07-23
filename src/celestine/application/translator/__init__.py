"""Application for translating text to other languages."""
import uuid
import requests
import os.path
import shutil
import keyword

from celestine.keyword.main import code
from celestine.keyword.main import language as language_list
from celestine.keyword.main import languages
from celestine.keyword.main import WRITE
from celestine.keyword.main import UTF_8


from celestine.keyword.translator import TRANSLATIONS
from celestine.keyword.translator import TEXT
from celestine.keyword.translator import TO

from celestine.application.translator.translator import Translator


# start: dict loader
from celestine.keyword import language
from celestine.keyword.unicode import LOW_LINE


def magic(module):
    dictionary = vars(module)
    return {
        key: value
        for key, value
        in dictionary.items()
        if not key.startswith(LOW_LINE)
    }


def magic1(dictionary):
    return {
        key: value
        for key, value
        in dictionary.items()
        if not key.startswith(LOW_LINE)
    }


def magic2(module):
    return magic1(vars(module))

# end: dict loader


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
        for name in language_list:
            path = os.path.join(self.directory, "celestine", "language", F"{name}.py")
            items = self.moose[name]
            with open(path, WRITE, encoding=UTF_8) as file:
                file.write(F'"""Lookup table for {name}."""\n')
                file.writelines(map(self.format_line, items))

    def parser_magic(self):
        """Do all parser stuff here."""
        for name in language_list:
            self.moose[name] = []

        thelist = magic2(language)
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


