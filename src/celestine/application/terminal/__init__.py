import configparser


from .keyword import CELESTINE


from celestine.application.terminal.keyword import APPLICATION
from celestine.application.terminal.keyword import LANGUAGE
from celestine.application.terminal.keyword import PYTHON


TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CELESTINE = "celestine"


def argument(argument):
    return argument


def attribute(attribute):
    """Build up the attribute file."""
    return attribute.add("terminal")


def default(default):
    """Build up the default file."""
    return default
