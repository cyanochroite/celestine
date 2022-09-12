"""Celestine Image Viewer"""
from celestine.session.argument import Argument
from celestine.session.attribute import Attribute

from celestine.core import load

from celestine.keyword.all import APPLICATION
from celestine.keyword.all import LANGUAGE
from celestine.keyword.all import TASK

PYTHON = "python"

PYTHON_3_6 = "python_3_6"
PYTHON_3_7 = "python_3_7"
PYTHON_3_8 = "python_3_8"
PYTHON_3_9 = "python_3_9"
PYTHON_3_10 = "python_3_10"
PYTHON_3_11 = "python_3_11"

from celestine.keyword.all import CELESTINE

class Session():
    def __init__(self, directory, args, exit_on_error):
        args = args or ["tkinter"]

        argument = Argument(exit_on_error)

        attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            load.module("internal"),
            CELESTINE,
        )

        module = load.module(APPLICATION, attribute.application)

        argument = module.argument(argument)
        attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            load.module("internal"),
            CELESTINE,
        )

        self.application = load.module(
            APPLICATION,
            attribute.application,
        )
        self.attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            module,
            attribute.application,
        )
        self.directory = directory  # me no like
        self.image_format = module.image_format()
        self.language = load.module(
            LANGUAGE,
            attribute.language,
        )
        self.python = self.python(
        )
        self.task = load.module(
            APPLICATION,
            attribute.application,
            attribute.task,
        )
        self.window = []
        #self.window.append(load.module("window", "main"))
        self.window.append(load.module("window", "zero"))
        self.window.append(load.module("window", "one"))
        self.window.append(load.module("window", "two"))

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

    def python(self):
        try:
            python = load.module(PYTHON, PYTHON_3_6)
            python = load.module(PYTHON, PYTHON_3_7)
            python = load.module(PYTHON, PYTHON_3_8)
            python = load.module(PYTHON, PYTHON_3_9)
            python = load.module(PYTHON, PYTHON_3_10)
            python = load.module(PYTHON, PYTHON_3_11)
        except SyntaxError:
            pass
        return python

    def main(self):
        return self.task.main(self)
