""""""
import os
import sys

sys.path[0] = os.path.dirname(sys.path[0])


half = "####################################"
split = f"{half}{half}"


celestine = __import__("celestine")
celestine.main(sys.argv[1:], True)


# Figure out how to recursivly call a package for all items in directory.
# Probably just find and copy how the others do it, with the best one.

# pydoccodestyle broken


""""""

import locale


def default():
    locale.getdefaultlocale()
    (language_code, encoding) = local.getdefaultlocale()
    language = language_code.split("_")[0]
    return language


# get prefs
# get default
# get english
# get last
