"""Application for translating text to other languages."""

from .report import main as train
from celestine.window.page import Page
import typing
import types
from celestine.session.argument import Argument

from celestine.text.unicode import NONE

from .text import KEY
from .text import REGION
from .text import URL


def add_argument(
    argument: Argument
) -> None:
    """Build up the argument."""

    argument.add_optional(
        KEY,
        "",
        NONE,
    )

    argument.add_optional(
        REGION,
        "",
        NONE,
    )

    argument.add_optional(
        URL,
        "",
        NONE,
    )


""""""


class Session():
    """"""

    @staticmethod
    def dictionary(
        _: types.ModuleType,
    ) -> typing.Dict[str, Argument]:
        """"""

        return {
        }


def report(page: Page):
    """"""
    with page.line("head") as line:
        line.label("title", "Page 0")
    label = train()
    for item in label:
        with page.line("body") as line:
            line.label(item, item)


def main(_: Session) -> list[typing.Callable[[Page], None]]:
    """"""
    return [
        report,
    ]
