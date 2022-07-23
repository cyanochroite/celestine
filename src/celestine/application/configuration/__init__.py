"""Generate configuration files for all packages."""
from celestine.application.configuration.argument import argument
from celestine.main.configuration import configuration_save
from celestine.main.configuration import configuration_celestine
from celestine.main.configuration import configuration_translator

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION_CELESTINE
from celestine.keyword.main import CONFIGURATION_TRANSLATOR


class Window():
    def __init__(self, session):
        self.session = session

    def file_dialog(self, tag, bind):
        pass

    def file_dialog_load(self, tag):
        pass

    def image(self, tag, image):
        pass

    def image_load(self, file):
        pass

    def label(self, tag, text):
        pass

    def _save(self, configuration, directory, file):
        configuration_save(configuration, directory, CELESTINE, file)

    def run(self, app):
        configuration = argument.configuration
        if configuration == "celestine":
            self._save(
                configuration_celestine(
                    argument.application,
                    argument.language,
                    argument.python,
                ),
                app.session.directory,
                CONFIGURATION_CELESTINE,
            )

        if configuration == "translator":
            self._save(
                configuration_translator(
                    argument.key,
                    argument.region,
                    argument.url,
                ),
                app.session.directory,
                CONFIGURATION_TRANSLATOR,
            )
