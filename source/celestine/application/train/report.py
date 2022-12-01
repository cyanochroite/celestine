"""Print out the lengths of the translations."""
from celestine.application.translator.parser import word_wrap_dictionary
from celestine.application.translator.parser import dictionary_to_file
from celestine.session import load

from celestine.application.translator.string import LANGUAGE
from celestine.application.translator.file import save

TRANSLATION = "translation"


def fix_source():
    translations = load.argument(TRANSLATION)
    for translation in translations:
        module = load.module(TRANSLATION, translation)
        dictionary = load.dictionary(module)

        path = load.python(TRANSLATION, translation)
        string = dictionary_to_file(dictionary)
        save(path, string)


def main():
    """The main function."""

    fix_source()

    minimum = {}
    maximum = {}

#    return []

    translations = load.argument(TRANSLATION)
    for translation in translations:
        module1 = load.module(TRANSLATION, translation)
        dictionary1 = load.dictionary(module1)

        module2 = load.module(LANGUAGE, translation)
        dictionary2 = load.dictionary(module2)

        dictionary2 |= dictionary1

        array = []
        for key, value in dictionary2.items():
            array.append((key, value))

        name = translation
        path = load.pathway(LANGUAGE, F"{name}.py")
        string = word_wrap_dictionary(dictionary2)
        save(path, string)

    label = []
    for key, value in minimum.items():
        label.append(F"{key}: min = {value} & max = {maximum[key]}")

    label.sort()
    return label

