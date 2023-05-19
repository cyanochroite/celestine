""""""

from celestine import load

LANGUAGE = "language"


def translate(*, session, **star):
    """Translate the language files."""

    dictionary = parser_magic(session)

    reset()

    # have way to provide default language?
    save_dictionary(dictionary["en"], LANGUAGE, INIT)

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
