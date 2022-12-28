""""""

from celestine.session import load
from celestine.session.parser import start_session

from celestine.text import CELESTINE
from celestine.text import VERSION_BLENDER
from celestine.text import VERSION_CELESTINE

from celestine.text.main import NAME
from celestine.text.main import DESCRIPTION_KEY
from celestine.text.main import DESCRIPTION_VALUE
from celestine.text.main import AUTHOR_KEY
from celestine.text.main import AUTHOR_VALUE
from celestine.text.main import VERSION
from celestine.text.main import BLENDER
from celestine.text.main import LOCATION_KEY
from celestine.text.main import LOCATION_VALUE
from celestine.text.main import WIKI_URL_KEY
from celestine.text.main import WIKI_URL_VALUE
from celestine.text.main import TRACKER_URL_KEY
from celestine.text.main import TRACKER_URL_VALUE
from celestine.text.main import SUPPORT_KEY
from celestine.text.main import SUPPORT_VALUE
from celestine.text.main import CATEGORY_KEY
from celestine.text.main import CATEGORY_VALUE

from celestine.text.directory import INTERFACE

bl_info = {
    NAME: CELESTINE,
    DESCRIPTION_KEY: DESCRIPTION_VALUE,
    AUTHOR_KEY: AUTHOR_VALUE,
    VERSION: VERSION_CELESTINE,
    BLENDER: VERSION_BLENDER,
    LOCATION_KEY: LOCATION_VALUE,
    WIKI_URL_KEY: WIKI_URL_VALUE,
    TRACKER_URL_KEY: TRACKER_URL_VALUE,
    SUPPORT_KEY: SUPPORT_VALUE,
    CATEGORY_KEY: CATEGORY_VALUE,
}


def register() -> None:
    """
    This is a function which only runs when enabling the add-on, this
    means the module can be loaded without activating the add-on.
    """
    load.module(INTERFACE, BLENDER).register()
    main([BLENDER], False)


def unregister() -> None:
    """
    This is a function to unload anything setup by register, this is
    called when the add-on is disabled.
    """
    load.module(INTERFACE, BLENDER).unregister()


def main(argv: list[str], exit_on_error: bool) -> None:
    """Run the main program."""
    session = start_session(argv, exit_on_error)
    with session.interface.window(session) as window:
        function = load.function_value(session.application)
        for document in function:
            window.page(document)
        window.turn_page = session.main
