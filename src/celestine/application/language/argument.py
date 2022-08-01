"""Generate configuration files for all packages."""
import argparse

from .keyword import CELESTINE
from .keyword import APPLICATION
from .keyword import LANGUAGE
from .keyword import TASK

from .keyword import KEY
from .keyword import REGION
from .keyword import URL

from .keyword import CONFIGURE
from .keyword import REPORT
from .keyword import TRANSLATE

from .keyword import STORE


parser = argparse.ArgumentParser(prog=CELESTINE)

parser.add_argument(
    APPLICATION,
    choices=[LANGUAGE],
    help="The currently run application.",
)

subparser = parser.add_subparsers(dest=TASK, required=True)

configure = subparser.add_parser(CONFIGURE, help="you are a fish")

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

report = subparser.add_parser(REPORT, help="you are a fish")

translate = subparser.add_parser(TRANSLATE, help="you are a fish")
