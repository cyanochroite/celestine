"""Application for translating text to other languages."""
from celestine.core import load

from celestine.application.terminal.argument import parser

from celestine.application.terminal.keyword import APPLICATION
from celestine.application.terminal.keyword import SESSION
from celestine.application.terminal.keyword import TERMINAL


def main(**kwargs):
    """def main"""
    session = kwargs[SESSION]

    argument = parser.parse_args()
    task = argument.task

    module = load.module(APPLICATION, TERMINAL, task)
    module.main(argument=argument, session=session)
