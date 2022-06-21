import sys
import os.path

current_directory = sys.path[0]
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from celestine.core.main import main
from celestine.data.exit import EXIT

from celestine.data.session import make
session = make(parent_directory)

exit = main(session)

if exit == EXIT.TEST:
    # Import everything so we can find tests.
    # This can only be done from the top level, so that is why it is here.
    from celestine.package.unittest import *
    # Also we only attempt to import unittest if the user requested it.
    # This is because it could not be installed and would error otherwise.
    import unittest
    unittest.main()
    # Program exits before reaching this line.

sys.exit(exit.value)
