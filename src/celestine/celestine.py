DEARPYGUI = True
PILLOW = True
TKINTER = True
UNITTEST = True

try:
    import dearpygui
except ModuleNotFoundError as error:
    DEARPYGUI = False

try:
    import PIL
except ModuleNotFoundError as error:
    PILLOW = False

try:
    import tkinter
except ModuleNotFoundError as error:
    TKINTER = False

try:
    import unittest
except ModuleNotFoundError as error:
    UNITTEST = False

PACKAGE = [
    DEARPYGUI,
    PILLOW,
    TKINTER,
    UNITTEST
]

print(PACKAGE)
