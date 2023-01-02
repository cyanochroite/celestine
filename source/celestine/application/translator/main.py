"""Application for translating text to other languages."""
from celestine.application.translator.file import save
from celestine.application.translator.text import LANGUAGE
from celestine.application.translator.parser import dictionary_to_file
from .text import LANGUAGE

import uuid
import os.path
import shutil
import requests

from celestine.session import load
from celestine.application.translator.translator import Translator


from .text import WRITE
from .text import UTF_8

from celestine.application.translator.parser import word_wrap_dictionary


TRANSLATION = "translation"


SESSION = "session"
TRANSLATIONS = "translations"
TEXT = "text"
TO = "to"


def parser_magic(session):
    """Do all parser stuff here."""
    dictionary = {}
    azure_to_iso = {}
    override = {}
    code = []

    dir_translation = load.argument(TRANSLATION)
    for translation in dir_translation:
        wow = load.dictionary(TRANSLATION, translation)

        key = wow["LANGUAGE_TAG_AZURE"]
        value = wow["LANGUAGE_TAG_ISO"]
        azure_to_iso[key] = value
        code.append(key)

        override[translation] = wow
        dictionary[translation] = {}

    thelist = load.dictionary("translation", "__init__")
    for name, value in thelist.items():

        items = post(session, code, value)
        for item in items:
            translations = item[TRANSLATIONS]
            for translation in translations:
                text = translation[TEXT]
                key = azure_to_iso[translation[TO]]
                dictionary[key][name] = text

    for translation in dir_translation:
        dictionary[translation] |= override[translation]

    return dictionary


def reset():
    """Remove the directory and rebuild it."""
    path = load.pathway(LANGUAGE)
    if os.path.islink(path):
        raise RuntimeError

    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=False, onerror=None)

    os.mkdir(path)


def header():
    """Write the header."""
    path = load.python(LANGUAGE, "__init__")
    with open(path, WRITE, encoding=UTF_8) as file:
        file.write('"""Lookup table for languages."""\n')


def save_item(dictionarys):
    """Save the items."""
    translations = load.argument(TRANSLATION)
    for translation in translations:
        dictionary = dictionarys[translation]
        path = load.python(LANGUAGE, translation)
        string = dictionary_to_file(dictionary)
        save(path, string)


def post(session, code, text):
    """Generate a post request."""
    translator = Translator(session.attribute)
    url = translator.endpoint()
    data = None
    json = [{TEXT: text}]
    headers = translator.header(str(uuid.uuid4()))
    params = translator.parameter(code)
    request = requests.post(url, data, json, headers=headers, params=params)
    return request.json()


def _translate(session):
    """def main"""

    dictionary = parser_magic(session)

    # directory stuff
    reset()
    header()

    save_item(dictionary)

    print(dictionary)
    print("done")
