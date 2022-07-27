"""Generate configuration files for all packages."""
import argparse

from celestine.keyword.main import CELESTINE

from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import language

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import application

from celestine.keyword.main import PYTHON
from celestine.keyword.main import python

from celestine.main.argument import parser


parser = argparse.ArgumentParser(add_help=False, prog="celestine")
parser.add_argument("application", choices=["language"])


subparser = parser.add_subparsers(dest="task", required=True)

configure = subparser.add_parser("configure")
configure.add_argument("key")
configure.add_argument("region")
configure.add_argument("url")

report = subparser.add_parser("report")

translate = subparser.add_parser("translate")
