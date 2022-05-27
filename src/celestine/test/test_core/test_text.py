import unittest

from celestine.core.text import *


class test_text(unittest.TestCase):
    def test_fatal(self):
        log.fatal("")

    def test_error(self):
        log.error("")

    def test_notice(self):
        log.notice("")

    def test_warning(self):
        log.warning("")

    def test_alert(self):
        log.alert("")

    def test_debug(self):
        log.debug("")

    def test_info(self):
        log.info("")

    def test_trace(self):
        log.trace("")
