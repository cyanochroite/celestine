"""This is the unittest file. It runs tests."""
import sys
import unittest

from celestine.test.test_parser.test_translator import *
from celestine.test.test_parser.test_operator import *

from celestine.test.test_extension.test_more_itertools import *

class Window():
    def __init__(self):
        pass

    def file_dialog(self, tag, bind):
        pass

    def file_dialog_load(self, tag):
        pass

    def image(self, tag, image):
        pass

    def image_load(self, file):
        pass

    def label(self, tag, text):
        pass

    def run(self, app):
        module="celestine.package.unittest"
        defaultTest=None #customize
        argv=[sys.argv[0]]#can we do better? sessios parent directiy
        testRunner=None
        testLoader=unittest.defaultTestLoader
        exit=True
        verbosity=2
        failfast=False
        catchbreak=True
        buffer=False
        warnings="error"
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