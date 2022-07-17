import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

import configparser

from celestine.main.configuration import configuration_save

from celestine_translator.keyword import AZURE

from celestine_translator.keyword import KEY
from celestine_translator.keyword import REGION
from celestine_translator.keyword import URL

from celestine_translator.keyword import FILE


key = ""  # secret
region = ""  # secret
url = ""  # secret


configuration = configparser.ConfigParser()

configuration.add_section(AZURE)
configuration.set(AZURE, KEY, key)
configuration.set(AZURE, REGION, region)
configuration.set(AZURE, URL, url)

path = os.path.join(directory, FILE)
configuration_save(path, configuration)
