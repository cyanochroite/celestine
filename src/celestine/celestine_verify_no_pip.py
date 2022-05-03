# Run this file if this was not installed with pip.
# Otherwise it can safely be deleted.
# Tests do not work from "__main__.py".
# Run them here instead.
import sys

try:
    import celestine
except ModuleNotFoundError:
    sys.path.insert(0, "../")

import unittest

from celestine.module.verify import *

unittest.main()
