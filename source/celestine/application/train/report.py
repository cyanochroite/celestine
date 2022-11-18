"""Print out the lengths of the translations."""
from celestine.session import load

from celestine.application.translator.string import LANGUAGE
from celestine.application.translator.file import File

TRANSLATION = "translation"


def main():
    """The main function."""
    minimum = {}
    maximum = {}

    translations = load.argument(TRANSLATION)
    for translation in translations:
        module1 = load.module(TRANSLATION, translation)
        dictionary1 = load.dictionary(module1)

        module2 = load.module(LANGUAGE, translation)
        dictionary2 = load.dictionary(module2)

        for key, value in dictionary1.items():
            dictionary2[key] = value

        array = []
        for key, value in dictionary2.items():
            array.append((key, value))

        name = translation
        file = File(name, F"Lookup table for {name}.", array)
        path = load.pathway(LANGUAGE, F"{name}.py")
        file.save(path)

    label = []
    for key, value in minimum.items():
        label.append(F"{key}: min = {value} & max = {maximum[key]}")

    label.sort()
    return label

