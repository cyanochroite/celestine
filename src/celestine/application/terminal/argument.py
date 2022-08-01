"""Generate configuration files for all packages."""
import argparse

from .keyword import CELESTINE
from .keyword import APPLICATION
from .keyword import TERMINAL
from .keyword import TASK

from .keyword import KEY
from .keyword import REGION
from .keyword import URL

from .keyword import CONFIGURE
from .keyword import REPORT
from .keyword import TRANSLATE


STORE = "store"

parser = argparse.ArgumentParser(prog=CELESTINE)
parser.add_argument(APPLICATION, choices=[TERMINAL])


subparser = parser.add_subparsers(dest=TASK, required=True)

configure = subparser.add_parser(CONFIGURE)

configure.add_argument(
    KEY,
    action=STORE,
    help ="A brief description of what the argument does.",
)

configure.add_argument(
    REGION,
    action=STORE,
    help ="A brief description of what the argument does.",
)

configure.add_argument(
    URL,
    action=STORE,
    help ="A brief description of what the argument does.",
)

report = subparser.add_parser(REPORT)

translate = subparser.add_parser(TRANSLATE)
