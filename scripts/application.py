"""Quick test of selected applications."""

import os
import sys

sys.path[0] = os.path.dirname(sys.path[0])

celestine = __import__("celestine")

celestine.main(["-l", "en"], True)
celestine.main(["-a", "demo", "-l", "en"], True)
celestine.main(["-a", "viewer", "-l", "en"], True)
