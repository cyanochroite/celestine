""""""

import unittest

from celestine.application.demo.__init__ import (
    main,
    one,
    two,
)
from celestine.session.parser import start_session
from celestine.window.page import Page

argv = ["-a", "demo"]


class test_init(unittest.TestCase):
    def test_one(self):
        """"""
        session = start_session(argv)
        page = Page(session)
        one(page)

    def test_two(self):
        """"""
        session = start_session(argv)
        page = Page(session)
        two(page)

    def test_main(self):
        """"""
        session = start_session(argv)
        page = Page(session)
        main(page)
