"""Application for translating text to other languages."""
from celestine.core import load

from celestine.application.language.argument import parser


"""Load and save user settings from a file."""

from celestine.main.configuration import configuration_save_main
from celestine.main.configuration import configuration_load_main

from celestine.keyword.main import APPLICATION
from celestine.application.language.keyword import LANGUAGE
from celestine.application.language.keyword import KEY
from celestine.application.language.keyword import REGION
from celestine.application.language.keyword import URL


from celestine.core import load

from celestine.keyword.main import language
from celestine.keyword.unicode import LOW_LINE




def main(**kwargs):
    """def main"""
    global session
    session = kwargs["session"]

    argument = parser.parse_args()
    task = argument.task

    if task == "configure":
        configuration = configuration_load_main(session.directory)

        if not configuration.has_section(LANGUAGE):
            configuration.add_section(LANGUAGE)
        configuration.set(LANGUAGE, KEY, argument.key)
        configuration.set(LANGUAGE, REGION, argument.region)
        configuration.set(LANGUAGE, URL, argument.url)

        configuration_save_main(configuration, session.directory)

    if task == "report":
        load.module(APPLICATION, LANGUAGE, task).main()

    if task == "euieui":
        configuration = configuration_load_main(directory)

        if not configuration.has_section(LANGUAGE):
            configuration.add_section(LANGUAGE)
        configuration.set(LANGUAGE, KEY, key)
        configuration.set(LANGUAGE, REGION, region)
        configuration.set(LANGUAGE, URL, url)

        configuration_save_main(configuration, directory)


