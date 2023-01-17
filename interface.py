"""Quick test of selected interfaces."""

import celestine

celestine.main(["-a", "demo", "-i", "curses", "-l", "en"], True)
celestine.main(["-a", "demo", "-i", "tkinter", "-l", "en"], True)
celestine.main(["-a", "demo", "-i", "dearpygui", "-l", "en"], True)
celestine.main(["-a", "demo", "-i", "pygame", "-l", "en"], True)
