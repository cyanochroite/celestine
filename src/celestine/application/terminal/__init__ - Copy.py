"""Generate configuration files for all packages."""
import argparse

from celestine.application.language.keyword import CELESTINE
from celestine.application.language.keyword import APPLICATION
from celestine.application.language.keyword import LANGUAGE
from celestine.application.language.keyword import TASK

from celestine.application.language.keyword import KEY
from celestine.application.language.keyword import REGION
from celestine.application.language.keyword import URL

from celestine.application.language.keyword import CONFIGURE
from celestine.application.language.keyword import REPORT
from celestine.application.language.keyword import TRANSLATE


parser = argparse.ArgumentParser(add_help=False, prog=CELESTINE)
parser.add_argument(APPLICATION, choices=[LANGUAGE])


subparser = parser.add_subparsers(dest=TASK, required=True)

configure = subparser.add_parser(CONFIGURE)
configure.add_argument(KEY)
configure.add_argument(REGION)
configure.add_argument(URL)

report = subparser.add_parser(REPORT)

translate = subparser.add_parser(TRANSLATE)
