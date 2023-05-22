"""Application for translating text to other languages."""
import os
import os.path
import shutil
import uuid

import requests

from celestine import load

from .data import (
    LANGUAGE,
    LANGUAGE_TAG_AZURE,
    LANGUAGE_TAG_ISO,
    TEXT,
    TO,
    TRANSLATIONS,
)
from .read import open_language
from .translator import Translator
from .write import (
    make_init_file,
    save_language,
)


def parser_magic(session, source):
    """Do all parser stuff here."""

    all_languages = {}

    azure_to_iso = {}
    dest_code = []

    language_list = load.argument(LANGUAGE)
    for language in language_list:
        head, body = open_language(LANGUAGE, language)

        key = body[LANGUAGE_TAG_AZURE]
        value = body[LANGUAGE_TAG_ISO]
        azure_to_iso[key] = value
        dest_code.append(key)

        all_languages[language] = {}
        all_languages[language]["name"] = language
        all_languages[language]["skip"] = body
        # all_languages[language]["work"] = {}

        # this because we skipped translator
        all_languages[language]["work"] = head

    source_list = load.dictionary(LANGUAGE, source)
    for name, value in source_list.items():
        continue  # disable post
        items = post(session, dest_code, value)
        for item in items:
            translations = item[TRANSLATIONS]
            for translation in translations:
                text = translation[TEXT]
                goto = translation[TO]
                language = azure_to_iso[goto]
                all_languages[language]["work"][name] = text

    return all_languages


def reset():
    """Remove the directory and rebuild it."""

    path = load.pathway(LANGUAGE)
    if os.path.islink(path):
        raise RuntimeError

    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=False, onerror=None)

    os.mkdir(path)


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

    reset()

    make_init_file()

    for key, value in dictionary.items():
        translation = value["work"]
        overridden = value["skip"]
        save_language(translation, overridden, LANGUAGE, key)

    print(dictionary)
    print("done")
