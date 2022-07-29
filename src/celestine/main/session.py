"""Load and save user settings from a file."""

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import PYTHON

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION_CELESTINE

CONFIGURATION = CONFIGURATION_CELESTINE

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_celestine

from celestine.core import load

import sys
import os.path
directory = os.path.dirname(sys.path[0])




PYTHON_3_6 = "python_3_6"
PYTHON_3_7 = "python_3_7"
PYTHON_3_8 = "python_3_8"
PYTHON_3_9 = "python_3_9"
PYTHON_3_10 = "python_3_10"
PYTHON_3_11 = "python_3_11"


from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import PYTHON

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION_CELESTINE

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_celestine

from celestine.core import load


PYTHON = "python"

PYTHON_3_6 = "python_3_6"
PYTHON_3_7 = "python_3_7"
PYTHON_3_8 = "python_3_8"
PYTHON_3_9 = "python_3_9"
PYTHON_3_10 = "python_3_10"
PYTHON_3_11 = "python_3_11"



default = configuration_celestine()

configuration = configuration_load(
    directory,
    CELESTINE,
    CONFIGURATION_CELESTINE
)

def load_application():
    try:
        argumentation = sys.argv[1]
        if argumentation not in applications:
            raise ValueError(applications)
    except IndexError:
        try:
            configuration = configuration_load(directory, CELESTINE, CONFIGURATION)
            argumentation = configuration[CELESTINE][APPLICATION]
        except KeyError:
            configuration = configuration_celestine()
            argumentation = configuration[CELESTINE][APPLICATION]
    return load.module(APPLICATION, argumentation)


def load_python():
    try:
        python = load.module(PYTHON, PYTHON_3_6)
        python = load.module(PYTHON, PYTHON_3_7)
        python = load.module(PYTHON, PYTHON_3_8)
        python = load.module(PYTHON, PYTHON_3_9)
        python = load.module(PYTHON, PYTHON_3_10)
        python = load.module(PYTHON, PYTHON_3_11)
    except SyntaxError:
        pass
    return python


application = load_application()
python = load_python()


