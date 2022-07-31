"""Package unittest."""
import unittest

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import CELESTINE
from celestine.keyword.main import UNITTEST


verify = None


def main(_):
    """def main"""
    module = F"{CELESTINE}.{APPLICATION}.verify"
    defaultTest = None
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
