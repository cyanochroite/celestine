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


from celestine.application.language.keyword import TRANSLATIONS
from celestine.application.language.keyword import TEXT
from celestine.application.language.keyword import TO

from celestine.application.language.translator import Translator


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


def reset():
    path = os.path.join(session.directory, "celestine", "language")
    if os.path.islink(path):
        raise RuntimeError

    if os.path.isdir(path):
        shutil.rmtree.avoids_symlink_attacks
        shutil.rmtree(path, ignore_errors=False, onerror=None)

    os.mkdir(path)


def header():
    path = os.path.join(session.directory, "celestine", "language", "__init__.py")
    with open(path, WRITE, encoding=UTF_8) as file:
        file.write(F'"""Lookup table for languages."""\n')


def format_line(item):
    (name, value) = item
    if not name.isidentifier():
        raise ValueError("Not a valid identifier.")
    if keyword.iskeyword(name) or keyword.issoftkeyword(name):
        raise ValueError("This work is a keyword.")
    value = value.replace('"', "'")
    return F'{name} = "{value}"\n'


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


def save_item():
    """Save the items."""
    for name in language_list:
        path = os.path.join(session.directory, "celestine", "language", F"{name}.py")
        items = moose[name]
        with open(path, WRITE, encoding=UTF_8) as file:
            file.write(F'"""Lookup table for {name}."""\n')
            file.writelines(map(format_line, items))


def parser_magic():
    """Do all parser stuff here."""
    for name in language_list:
        moose[name] = []

    thelist = magic2(language)
    for name, value in thelist.items():
        add_item(name, value)


def main(**kwargs):
    """def main"""
    global session
    session = kwargs["session"]

    global moose
    moose = {}

    parser_magic()

    reset()
    header()
    save_item()

    print(moose)
    print("done")
