""""""

from celestine import load

from celestine.unicode import QUOTATION_MARK
from celestine.unicode import LINE_FEED
from celestine.file import save_module

from .main import parser_magic
from .main import reset
from .main import save_dictionary
import io

LANGUAGE = "language"
INIT = "__init__"

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

    reset()

    make_init_file()

    for key, value in dictionary.items():
        save_dictionary(value, LANGUAGE, key)

    print(dictionary)
    print("done")


def train():
    """The main function."""
    minimum = {}
    maximum = {}
    language = load.argument(LANGUAGE)
    for lang in language:
        dictionary = load.dictionary(LANGUAGE, lang)
        for key, value in dictionary.items():
            length = len(value)
            minimum[key] = min(length, minimum.get(key, 256))
            maximum[key] = max(length, maximum.get(key, 0))

    return {"min": minimum, "max": maximum}
