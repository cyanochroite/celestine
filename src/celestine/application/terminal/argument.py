"""Generate configuration files for all packages."""
import argparse

from celestine.application.terminal.keyword import CELESTINE
from celestine.application.terminal.keyword import APPLICATION
from celestine.application.terminal.keyword import LANGUAGE
from celestine.application.terminal.keyword import TASK

from celestine.application.terminal.keyword import KEY
from celestine.application.terminal.keyword import REGION
from celestine.application.terminal.keyword import URL

from celestine.application.terminal.keyword import CONFIGURE
from celestine.application.terminal.keyword import REPORT
from celestine.application.terminal.keyword import TRANSLATE


parser = argparse.ArgumentParser(add_help=False, prog=CELESTINE)
parser.add_argument(APPLICATION, choices=[LANGUAGE])


subparser = parser.add_subparsers(dest=TASK, required=True)

configure = subparser.add_parser(CONFIGURE)
configure.add_argument(KEY)
configure.add_argument(REGION)
configure.add_argument(URL)

report = subparser.add_parser(REPORT)

translate = subparser.add_parser(TRANSLATE)
