"""Quick test of selected interfaces."""

import os
import sys

sys.path[0] = os.path.dirname(sys.path[0])

celestine = __import__("celestine")

celestine.main(["-a", "demo", "-i", "curses", "-l", "en"], True)
celestine.main(["-a", "demo", "-i", "tkinter", "-l", "en"], True)
celestine.main(["-a", "demo", "-i", "dearpygui", "-l", "en"], True)
celestine.main(["-a", "demo", "-i", "pygame", "-l", "en"], True)
