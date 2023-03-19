""""""

import unittest

from celestine.application.demo import (
    main,
    one,
    two,
)
from celestine.interface.tkinter.container import Container
from celestine.session.parser import start_session

argv = ["-a", "demo"]


class InitTest(unittest.TestCase):
    """"""

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
