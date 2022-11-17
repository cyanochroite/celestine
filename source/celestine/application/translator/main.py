"""Application for translating text to other languages."""
from celestine.session import load
from celestine.application.translator.file import File
from celestine.application.translator.translator import Translator
import uuid
import os.path
import shutil


import requests


from celestine.keywords.all import code
from celestine.keywords.all import language as language_list
from celestine.keywords.all import languages
from celestine.keywords.all import WRITE
from celestine.keywords.all import UTF_8


SESSION = "session"
TRANSLATIONS = "translations"
TEXT = "text"
TO = "to"


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
    path = os.path.join(session.directory, "celestine",
                        "language", "__init__.py")
    with open(path, WRITE, encoding=UTF_8) as file:
        file.write('"""Lookup table for languages."""\n')


def save_item():
    """Save the items."""
    for name in language_list:
        file = File(name, F"Lookup table for {name}.", moose[name])
        file.save(session.directory, "celestine", "language")


def post(text):
    """Generate a post request."""
    translator = Translator(session.attribute)
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


def main(a_session):
    """def main"""
    global session
    session = a_session
    global moose
    moose = {}

    parser_magic()

    reset()
    header()

    save_item()

    print(moose)
    print("done")
