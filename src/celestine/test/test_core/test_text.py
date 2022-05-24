import unittest

from celestine.core.text import *


class test_text(unittest.TestCase):
    def test_fatal(self):
        log.fatal("text")

    def test_error(self):
        log.error("text")

    def test_notice(self):
        log.notice("text")

    def test_warning(self):
        log.warning("text")

    def test_alert(self):
        log.alert("text")

    def test_debug(self):
        log.debug("text")

    def test_info(self):
        log.info("text")

    def test_trace(self):
        log.trace("text")
