""""""

import unittest

from celestine.application.demo.__init__ import (
    main,
    one,
    two,
)
from celestine.session.parser import start_session
from celestine.window.container import Container

argv = ["-a", "demo"]


class test_init(unittest.TestCase):
    def test_one(self):
        """"""
        name = "one"
        session = start_session(argv)
        container = Container(session, "window", None)
        page = container.drop(name)
        one(page)

    def test_two(self):
        """"""
        name = "two"
        session = start_session(argv)
        container = Container(session, "window", None)
        page = container.drop(name)
        two(page)

    def test_main(self):
        """"""
        name = "main"
        session = start_session(argv)
        container = Container(session, "window", None)
        page = container.drop(name)
        main(page)
