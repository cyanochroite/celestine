"""Application for translating text to other languages."""
import os
import os.path
import shutil
import uuid

import requests

from celestine import load
from celestine.file import open_module

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


import io

from celestine import load
from celestine.application.translator.parser import dictionary_to_file
from celestine.file import save_module
from celestine.unicode import (
    LINE_FEED,
    QUOTATION_MARK,
)

LANGUAGE = "language"
INIT = "__init__"

##########################


def save_dictionary(dictionary, *path):
    """Convert a dictionary to a string and save it to a file."""
    string = dictionary_to_file(dictionary)
    save_module(string, *path)


###########################


def make_init_file():
    """"""
    string = io.StringIO()
    string.write(QUOTATION_MARK)
    string.write(QUOTATION_MARK)
    string.write(QUOTATION_MARK)
    string.write(QUOTATION_MARK)
    string.write(QUOTATION_MARK)
    string.write(QUOTATION_MARK)
    string.write(LINE_FEED)

    value = string.getvalue()
    save_module(value, LANGUAGE, INIT)


def translate(*, session, **star):
    """Translate the language files."""

    # Add ability to choose master language file.
    source = "en"

    dictionary = parser_magic(session, source)

    # reset()

    # make_init_file()

    for key, value in dictionary.items():
        save_dictionary(value, LANGUAGE, key)

    print(dictionary)
    print("done")


def open_language(*path):
    """Convert a dictionary to a string and save it to a file."""

    string = io.StringIO()
    half = "####################################"
    whole = f"{half}{half}"

    for line in open_module(*path):
        string.write(line)

    value = string.getvalue()
    split = value.split(whole)

    head = split[0]
    body = split[1]

    return (head, body)


##########


def parser_magic(session, source):
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


def parser_magic(session):
    """Do all parser stuff here."""

    dictionary = {}
    azure_to_iso = {}
    override = {}
    code = []

    language_list = load.argument(LANGUAGE)
    for language in language_list:
        open_language(LANGUAGE, language)

        wow = load.dictionary(LANGUAGE, language)

        key = wow[LANGUAGE_TAG_AZURE]
        value = wow[LANGUAGE_TAG_ISO]
        azure_to_iso[key] = value
        code.append(key)

        override[language] = wow
        dictionary[language] = {}

    return dictionary


##############


def parser_magic(session, source):
    """Do all parser stuff here."""

    dictionary = {}
    azure_to_iso = {}
    dest_code = []

    override = {}

    dir_translation = load.argument(LANGUAGE)
    for translation in dir_translation:
        wow = load.dictionary(LANGUAGE, translation)

        key = wow[LANGUAGE_TAG_AZURE]
        value = wow[LANGUAGE_TAG_ISO]
        azure_to_iso[key] = value
        dest_code.append(key)

        override[translation] = wow
        dictionary[translation] = {}

    the_list = load.dictionary(LANGUAGE, source)
    for name, value in the_list.items():
        continue  # disable post
        items = post(session, dest_code, value)
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


def do_translate(session):
    """Translate the language files."""

    # Add ability to choose master language file.
    source = "en"

    dictionary = parser_magic(session, source)

    # reset()

    # make_init_file()

    for key, value in dictionary.items():
        save_dictionary(value, LANGUAGE, key)

    print(dictionary)
    print("done")
