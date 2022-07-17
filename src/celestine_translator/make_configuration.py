import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

import configparser

from celestine.main.configuration import configuration_save



from celestine.main.keyword import APPLICATION

from celestine.main.keyword import LANGUAGE
from celestine.main.keyword import ENGLISH

from celestine.main.keyword import PACKAGE
from celestine.main.keyword import CELESTINE

from celestine.main.keyword import PYTHON
from celestine.main.keyword import PYTHON_3_10


configuration = configparser.ConfigParser()

configuration.add_section(APPLICATION)
configuration.set(APPLICATION, LANGUAGE, ENGLISH)
configuration.set(APPLICATION, PACKAGE, CELESTINE)
configuration.set(APPLICATION, PYTHON, PYTHON_3_10)

path = os.path.join(directory, CELESTINE, "celestine.ini")
configuration_save(path, configuration)
