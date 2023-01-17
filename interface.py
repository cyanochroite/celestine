"""Quick test of selected interfaces."""

import celestine

celestine.main(["demo", "-i", "curses", "-l", "en"], True)
celestine.main(["demo", "-i", "tkinter", "-l", "en"], True)
celestine.main(["demo", "-i", "dearpygui", "-l", "en"], True)
celestine.main(["demo", "-i", "pygame", "-l", "en"], True)
