"""Celestine Image Viewer"""
from celestine.session.argument import Argument
from celestine.session.attribute import Attribute

from celestine.session import load


from celestine.keyword.all import APPLICATION
from celestine.keyword.all import CELESTINE

from celestine.keyword.all import INTERFACE
from celestine.keyword.all import LANGUAGE
from celestine.keyword.all import PYTHON


import celestine.session.argument as fish

TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CONFIGURE = "configure"
STORE = "store"
TKINTER = "tkinter"
EN = "en"


class Session():
    def __init__(self, args, exit_on_error):
        language = fish.fast_pass(args, exit_on_error)
        translate = load.module(LANGUAGE, language)

        # temp until translation happen
        translate = load.module("keyword", "translation")

        directory = ""
        print(directory)

        argument = Argument(exit_on_error, translate)

        default1 = ("tkinter", ENGLISH, PYTHON_3_10, "main")
        attribute1 = (APPLICATION, LANGUAGE, PYTHON, "task")

        default1 = (TKINTER, "en", "main")
        attribute1 = (INTERFACE, LANGUAGE, "task")

        default1 = (
            load.argument_default(INTERFACE),
            load.argument_default(PYTHON),
            EN,
        )
        attribute1 = (INTERFACE, PYTHON, LANGUAGE)

        attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            attribute1,
            default1,
            CELESTINE,
        )

        module = load.module(INTERFACE, attribute.interface)

        argument = module.argument(argument)
        attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            attribute1,
            default1,
            CELESTINE,
        )

        self.application = load.module(
            INTERFACE,
            attribute.interface,
        )
        self.attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            module.attribute(),
            module.default(),
            attribute.interface,
        )
        self.image_format = module.image_format()
        self.language = load.module(
            LANGUAGE,
            attribute.language,
        )
        self.python = attribute.python
        self.task = load.module(
            INTERFACE,
            attribute.interface,
        )
