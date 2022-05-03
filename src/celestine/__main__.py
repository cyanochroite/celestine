import sys

try:
    # Check to see if this installed as a global package.
    import celestine
except ModuleNotFoundError:
    # If not then we will need to search for files from the parent directory.
    sys.path.insert(0, "../")

from celestine.enum.exit import EXIT
from celestine.main import main

exit = main()

if exit == EXIT.TEST:
    # Clear argument list before we call unittest.
    sys.argv = [sys.argv[0]]
    # Import everything so we can find tests.
    # This can only be done from the top level, so that is why it is here.
    from celestine.module.verify import *
    import unittest
    unittest.main()
    # Program exits before reaching this line.

sys.exit(exit)
