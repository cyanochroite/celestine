"""Package unittest."""
import unittest

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import CELESTINE
from celestine.keyword.main import UNITTEST

from celestine.application.unittest.parser.test_translator import *
from celestine.application.unittest.parser.test_operator import *

from celestine.application.unittest.extension.test_more_itertools import *
from celestine.application.unittest.core.test_text import *


def main(_):
    """def main"""
    module = F"{CELESTINE}.{APPLICATION}.{UNITTEST}"
    defaultTest = None  # customize
    argv = [CELESTINE]
    testRunner = None
    testLoader = unittest.defaultTestLoader
    exit = True
    verbosity = 2
    failfast = False
    catchbreak = True
    buffer = True
    warnings = "error"
    unittest.main(
        module,
        defaultTest,
        argv,
        testRunner,
        testLoader,
        exit,
        verbosity,
        failfast,
        catchbreak,
        buffer,
        warnings
    )


def main(_):
    """def main"""
    module = F"{CELESTINE}.{APPLICATION}.{UNITTEST}"
    defaultTest = ["test_text"]
    argv = [CELESTINE]
    testRunner = None
    testLoader = unittest.defaultTestLoader
    exit = True
    verbosity = 2
    failfast = False
    catchbreak = True
    buffer = True
    warnings = "error"
    unittest.main(
        module,
        defaultTest,
        argv,
        testRunner,
        testLoader,
        exit,
        verbosity,
        failfast,
        catchbreak,
        buffer,
        warnings
    )
