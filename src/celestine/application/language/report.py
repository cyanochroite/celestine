"""Print out the lengths of the translations."""
from celestine.core import load

from celestine.application.language.keyword import language
from celestine.application.language.keyword import LANGUAGE


def main(**_):
    """The main function."""
    minimum = {}
    maximum = {}

    for lang in language:
        module = load.module(LANGUAGE, lang)
        dictionary = load.dictionary(module)
        for key, value in dictionary.items():
            length = len(value)
            minimum[key] = min(length, minimum.get(key, 256))
            maximum[key] = max(length, maximum.get(key, 0))

    print(minimum)
    print(maximum)
