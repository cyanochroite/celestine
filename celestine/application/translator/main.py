"""Application for translating text to other languages."""
import os
import os.path
import shutil
import uuid

import requests

from celestine import load

from .file import save_dictionary
from .text import LANGUAGE
from .translator import Translator

INIT = "__init__"


TRANSLATION = "translation"


SESSION = "session"
TRANSLATIONS = "translations"
TEXT = "text"
TO = "to"

LANGUAGE_TAG_AZURE = "LANGUAGE_TAG_AZURE"
LANGUAGE_TAG_ISO = "LANGUAGE_TAG_ISO"


def parser_magic(session):
    """Do all parser stuff here."""
    dictionary = {}
    azure_to_iso = {}
    override = {}
    code = []

    dir_translation = load.argument(TRANSLATION)
    for translation in dir_translation:
        wow = load.dictionary(TRANSLATION, translation)

        key = wow[LANGUAGE_TAG_AZURE]
        value = wow[LANGUAGE_TAG_ISO]
        azure_to_iso[key] = value
        code.append(key)

        override[translation] = wow
        dictionary[translation] = {}

    thelist = load.dictionary("translation", "__init__")
    # thelist = {}
    for name, value in thelist.items():
        items = post(session, code, value)
        for item in items:
            translations = item[TRANSLATIONS]
            for translation in translations:
                text = translation[TEXT]
                goto = translation[TO]
                key = azure_to_iso[goto]
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


def save_item(dictionarys):
    """Save the items."""
    translations = load.argument(TRANSLATION)
    for translation in translations:
        dictionary = dictionarys[translation]
        save_dictionary(dictionary, LANGUAGE, translation)


def post(session, code, text):
    """Generate a post request."""
    translator = Translator(session.attribute)
    url = translator.endpoint()
    data = None
    json = [{TEXT: text}]
    headers = translator.header(str(uuid.uuid4()))
    params = translator.parameter(code)
    request = requests.post(
        url, data, json, headers=headers, params=params
    )
    return request.json()


def _translate(session):
    """def main"""

    do = load.dictionary("language", "en")
    save_dictionary(do, "")
    #

    dictionary = parser_magic(session)

    reset()

    # have way to provide default language?
    save_dictionary(dictionary["en"], LANGUAGE, INIT)

    for key, value in dictionary.items():
        save_dictionary(value, LANGUAGE, key)

    print(dictionary)
    print("done")
