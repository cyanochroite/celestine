"""Print out the lengths of the translations."""
from celestine.session import load

from celestine.application.translator.string import LANGUAGE


def main():
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

    label = []
    for key, value in minimum.items():
        label.append(F"{key}: min = {value} & max = {maximum[key]}")

    label.sort()
    return label
