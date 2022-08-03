"""Application for translating text to other languages."""
from celestine.core import load

from .argument import argument as argmain

from .keyword import APPLICATION
from .keyword import LANGUAGE


def main(session):
    """def main"""

    #    argument = argmain(session).parse_args()
    argmain(session)
    argument = session.parse(session)
    task = argument.task

    module = load.module(APPLICATION, LANGUAGE, task)
    module.main(argument=argument, session=session)
