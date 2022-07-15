import configparser

import os.path
import sys
directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

from celestine.main.keyword import language
from celestine.main.keyword import languages
from celestine.main import configuration

TRANSLATIONS = "translations"
TEXT = "text"
TO = "to"

moose = {}


def new_parser():
    for name in language:
        moose[name] = configparser.ConfigParser()


def add_section(section):
    for name in language:
        moose[name].add_section(section)


def add_item(section, key, value):
    for name in language:
        moose[name].set(section, key, value)


def save_item():
    for name in language:
        path = os.path.join(directory, "celestine", "language", F"{name}.ini")
        configuration.save(path, moose[name])


file = os.path.join(directory, "celestine_translator", "language.ini")
config = configuration.load(file)
mydict = vars(config)["_sections"]

new_parser()
for section, dictionary in mydict.items():
    add_section(section)
    for key, value in dictionary.items():
        add_item(section, key, value)

save_item()


print(moose)


def stuff(items):
    for item in items:
        translations = item[TRANSLATIONS]
        for translation in translations:
            text = translation[TEXT]
            to = translation[TO]
            put = languages[to]
            figtree[put].append(text)

