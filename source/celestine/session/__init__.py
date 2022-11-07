"""Celestine Image Viewer"""
from celestine.session.argument import Argument
from celestine.session.attribute import Attribute
from celestine.session import python

from celestine.session import load

from celestine.keyword.all import APPLICATION
from celestine.keyword.all import CELESTINE
from celestine.keyword.all import LANGUAGE
from celestine.keyword.all import CELESTINE


from celestine.keyword.all import APPLICATION
from celestine.keyword.all import LANGUAGE
from celestine.keyword.all import PYTHON

from celestine.keyword.all import application
from celestine.keyword.all import language


APPLICATION = "package"

TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CONFIGURE = "configure"
STORE = "store"


class Session():
    def __init__(self, args, exit_on_error):
        directory = ""
        args = args or ["tkinter"]

        argument = Argument(exit_on_error)

        default1 = ("tkinter", ENGLISH, PYTHON_3_10, "main")
        attribute1 = (APPLICATION, LANGUAGE, PYTHON, "task")

        attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            attribute1,
            default1,
            CELESTINE,
        )

        attribute.application = attribute.package
        module = load.module(APPLICATION, attribute.application)

        argument = module.argument(argument)
        attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            attribute1,
            default1,
            CELESTINE,
        )
        attribute.application = attribute.package

        self.application = load.module(
            APPLICATION,
            attribute.application,
        )
        self.attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            module.attribute(),
            module.default(),
            attribute.application,
        )
        self.image_format = module.image_format()
        self.language = load.module(
            LANGUAGE,
            attribute.language,
        )
        self.python = python.version()
        self.task = load.module(
            APPLICATION,
            attribute.application,
        )

    def add_configuration(self, configuration, module, application):
        """Build up the configuration file."""
        if not configuration.has_section(application):
            configuration.add_section(application)
        attribute = module.attribute()
        default = module.default()
        for item in zip(attribute, default, strict=True):
            (name, value) = item
            configuration.set(application, name, value)

        return configuration
