"""Application for translating text to other languages."""
import uuid
import os.path
import shutil
import requests


from celestine.keyword.main import code
from celestine.keyword.main import language as language_list
from celestine.keyword.main import languages
from celestine.keyword.main import WRITE
from celestine.keyword.main import UTF_8


from celestine.application.language.keyword import SESSION
from celestine.application.language.keyword import TRANSLATIONS
from celestine.application.language.keyword import TEXT
from celestine.application.language.keyword import TO

from celestine.application.language.translator import Translator

from celestine.core import load
from celestine.core.file import File


def parser_magic():
    """Do all parser stuff here."""
    for name in language_list:
        moose[name] = []

    module = load.module("keyword", "language")
    thelist = load.dictionary(module)
    for name, value in thelist.items():
        add_item(name, value)

def reset():
    """Remove the directory and rebuild it."""
    path = os.path.join(session.directory, "celestine", "language")
    if os.path.islink(path):
        raise RuntimeError

    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=False, onerror=None)

    os.mkdir(path)


def header():
    """Write the header."""
    path = os.path.join(session.directory, "celestine", "language", "__init__.py")
    with open(path, WRITE, encoding=UTF_8) as file:
        file.write('"""Lookup table for languages."""\n')


def save_item():
    """Save the items."""
    for name in language_list:
        file = File(name, F"Lookup table for {name}.", moose[name])
        file.save(session.directory, "celestine", "language")


def post(text):
    """Generate a post request."""
    translator = Translator(session.directory)
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


def main(**kwargs):
    """def main"""
    global session
    session = kwargs[SESSION]

    global moose
    moose = {}

    parser_magic()

    reset()
    header()

    save_item()

    print(moose)
    print("done")
