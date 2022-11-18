"""Print out the lengths of the translations."""
from celestine.session import load

from .string import LANGUAGE


def main(_):
    """The main function."""
    minimum = {}
    maximum = {}

    languages = load.argument(LANGUAGE)
    for language in languages:
        module = load.module(LANGUAGE, language)
        dictionary = load.dictionary(module)
        for key, value in dictionary.items():
            length = len(value)
            minimum[key] = min(length, minimum.get(key, 256))
            maximum[key] = max(length, maximum.get(key, 0))

    print(minimum)
    print(maximum)
