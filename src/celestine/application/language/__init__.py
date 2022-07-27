"""Application for translating text to other languages."""
from celestine.core import load

from celestine.application.language.argument import parser


def main(**kwargs):
    """def main"""
    global session
    session = kwargs["session"]

    argument = parser.parse_args()
    task = argument.task

    load.module("application", "language", task).configure(session.directory)
