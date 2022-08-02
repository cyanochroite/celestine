"""Generate configuration files for all packages."""
import argparse

from .keyword import KEY
from .keyword import REGION
from .keyword import URL

from .keyword import CONFIGURE
from .keyword import REPORT
from .keyword import TRANSLATE

from .keyword import STORE


def argument(session):
    configure = session.argument.subparser.add_parser(
        CONFIGURE,
        help="you are a fish",
    )
    
    configure.add_argument(
        KEY,
        action=STORE,
        help="A brief description of what the argument does.",
    )
    
    configure.add_argument(
        REGION,
        action=STORE,
        help="A brief description of what the argument does.",
    )
    
    configure.add_argument(
        URL,
        action=STORE,
        help="A brief description of what the argument does.",
    )
    
    
    report = session.argument.subparser.add_parser(
        REPORT,
        help="you are a fish",
    )
    
    
    translate = session.argument.subparser.add_parser(
        TRANSLATE,
        help="you are a fish",
    )
