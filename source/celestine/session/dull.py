"""Celestine Image Viewer"""

import typing

from celestine.session.argument import Argument
from celestine.session.argument import Information

from .text import CONFIGURATION
from .text import HELP
from .text import STORE_TRUE
from .text import VERSION


class Session():
    """"""

    @staticmethod
    def dictionary(
        language,
    ) -> typing.Dict[str, Argument]:
        """"""

        return {
            CONFIGURATION: Information(
                "",
                STORE_TRUE,
                language.ARGUMENT_HELP_HELP,
                False,
            ),
            HELP: Information(
                "",
                HELP,
                language.ARGUMENT_HELP_HELP,
                False,
            ),
            VERSION: Information(
                "",
                VERSION,
                language.ARGUMENT_VERSION_HELP,
                True,
            ),
        }
