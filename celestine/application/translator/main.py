"""Application for translating text to other languages."""
import io
import keyword
import os
import os.path
import shutil
import uuid

import requests

from celestine.unicode import (
    APOSTROPHE,
    INFORMATION_SEPARATOR_FOUR,
    INFORMATION_SEPARATOR_ONE,
    INFORMATION_SEPARATOR_THREE,
    INFORMATION_SEPARATOR_TWO,
    LINE_SEPARATOR,
    PARAGRAPH_SEPARATOR,

    LINE_FEED,
    QUOTATION_MARK,
    REVERSE_SOLIDUS,
    SPACE,
)


from celestine import load
from celestine.alphabet import UNICODE
from celestine.file import (
    normalize,
    open_module,
    save_module,
)
from celestine.unicode import (
    EQUALS_SIGN,
    FULL_STOP,
    INFORMATION_SEPARATOR_FOUR,
    LINE_FEED,
    QUOTATION_MARK,
    REVERSE_SOLIDUS,
    SPACE,
)

from .data import LANGUAGE

from .data import (
    SESSION,
    TRANSLATIONS,
    TEXT,
    TO,
    LANGUAGE_TAG_AZURE,
    LANGUAGE_TAG_ISO,
    INIT,
    )


from .translator import Translator


def do_normalize(string):
    """"""
    character = normalize.character(string)
    whitespace = normalize.whitespace(character)
    quotation = normalize.quotation(whitespace)
    punctuation = normalize.punctuation(quotation)
    yield from punctuation


def assignment_expression(identifier, expression):
    """
    Make a line for the file from a key value pair.

    return F'{identifier} = "{expression}"\n'
    """
    if not identifier.isidentifier():
        raise ValueError("Not a valid identifier.")
    if keyword.iskeyword(identifier):
        raise ValueError("This word is a keyword.")
    if keyword.issoftkeyword(identifier):
        raise ValueError("This word is a soft keyword.")

    yield from LINE_FEED
    yield from LINE_SEPARATOR
    yield from identifier
    yield from SPACE
    yield from EQUALS_SIGN
    yield from SPACE
    yield from QUOTATION_MARK
    yield from INFORMATION_SEPARATOR_FOUR
    yield from do_normalize(expression)
    yield from QUOTATION_MARK
    yield from LINE_FEED
    yield from LINE_SEPARATOR



def transverse_dictionary(dictionary):
    """"""
    items = dictionary.items()
    sorted_items = sorted(items)
    for key, value in sorted_items:
        yield from assignment_expression(key, value)


##########################


def language_file(translation, overridden):
    """Print translations first then print overridden values."""
    lookup = translation | overridden
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from lookup["LANGUAGE_NAME_ENGLISH"]
    yield from SPACE
    yield from lookup["LANGUAGE_NAME_NATIVE"]
    yield from SPACE
    yield from lookup["LANGUAGE_TAG_ISO"]
    yield from FULL_STOP
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from LINE_FEED
    yield from LINE_SEPARATOR

    yield from transverse_dictionary(translation)

    yield from PARAGRAPH_SEPARATOR

    yield from transverse_dictionary(overridden)



def save_language(translation, overridden, *path):
    """"""
    file = language_file(translation, overridden)
    string = normalize.width(file)
    save_module(string, *path)


def fix_line_split(*path):
    """"""
    skip = False

    document = open_module(*path)
    for string in document:
        for character in string:
            if character not in UNICODE:
                continue

            if character == REVERSE_SOLIDUS:
                skip = True
                continue

            if skip:
                skip = False
                continue

            yield from character


def read_new_lines(string):
    """"""

    buffer = io.StringIO()
    count = 0

    for character in string:
        count += buffer.write(character)

        if character == LINE_FEED:
            buffer.seek(0, io.SEEK_SET)
            line = buffer.read(count)
            buffer.seek(0, io.SEEK_SET)
            count = 0
            yield from line


###########################


def make_dictionary(document):
    dictionary = {}

    lines = document.split(LINE_FEED)
    for line in lines:
        if line[0:3] == '"""':
            continue

        if not line:
            continue
        split = line.split("=")
        key = split[0].strip()
        value = split[-1].strip()[1:-1]
        dictionary[key] = value
    return dictionary


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
    string.write(LINE_SEPARATOR)

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

    text = fix_line_split(*path)
    lines = read_new_lines(text)
    # normal = normalize(lines)
    normal = lines

    string = io.StringIO()
    for line in normal:
        string.write(line)

    value = string.getvalue()

    half = "####################################"
    whole = f"{half}{half}"

    split = value.split(whole)

    head = split[0]
    body = split[-1]

    return (head, body)


##############


def parser_magic(session, source):
    """Do all parser stuff here."""

    all_languages = {}

    azure_to_iso = {}
    dest_code = []

    language_list = load.argument(LANGUAGE)
    for language in language_list:
        head, body = open_language(LANGUAGE, language)
        head = make_dictionary(head)
        body = make_dictionary(body)

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


def save_item(dictionarys):
    """Save the items."""
    translations = load.argument(LANGUAGE)
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
        translation = value["work"]
        overridden = value["skip"]
        save_language(translation, overridden, LANGUAGE, key)

    print(dictionary)
    print("done")
