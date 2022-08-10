"""Package unittest."""
from celestine.application.verify.core.test_text import test_text


from celestine.application.verify.extension.test_more_itertools import test_more_itertools


from celestine.application.verify.parser.test_operator import test_digit
from celestine.application.verify.parser.test_operator import test_unary
from celestine.application.verify.parser.test_operator import test_comparison

from celestine.application.verify.parser.test_translator import test_translator


def argument(argument):
    """Build up the argument."""
    return argument


def configuration(configuration):
    """Build up the configuration file."""
    return configuration


def default(default):
    """Build up the default file."""
    return default
