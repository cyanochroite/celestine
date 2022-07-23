"""Package unittest."""
import unittest

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import CELESTINE
from celestine.keyword.main import UNITTEST

from celestine.tests.test_parser.test_translator import *
from celestine.tests.test_parser.test_operator import *

from celestine.tests.test_extension.test_more_itertools import *


class Window():
    def __init__(self, session):
        self.session = session

    def file_dialog(self, tag, bind):
        """pass"""
        pass

    def file_dialog_load(self, tag):
        """pass"""
        pass

    def image(self, tag, image):
        """pass"""
        pass

    def image_load(self, file):
        """pass"""
        pass

    def label(self, tag, text):
        """pass"""
        pass

    def run(self, app):
        """pass"""
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
