"""Application for translating text to other languages."""
from celestine.core import load

from celestine.application.language.argument import parser


from celestine.application.language.keyword import APPLICATION
from celestine.application.language.keyword import LANGUAGE
from celestine.application.language.keyword import SESSION


def main(**kwargs):
    """def main"""
    session = kwargs[SESSION]

    argument = parser.parse_args()
    task = argument.task

    module = load.module(APPLICATION, LANGUAGE, task)
    module.main(argument=argument, session=session)
