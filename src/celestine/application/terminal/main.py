"""Application for translating text to other languages."""
from celestine.core import load

from .argument import parser
from .keyword import APPLICATION
from .keyword import TERMINAL


def main(session):
    """def main"""
    argument = parser.parse_args()
    task = argument.task

    module = load.module(APPLICATION, TERMINAL, task)
    module.main(argument=argument, session=session)
