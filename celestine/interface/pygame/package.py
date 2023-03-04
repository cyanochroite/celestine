""""""

# import pygame
import os
import sys

from celestine.text.stream import UTF_8

PYGAME = None


class HiddenPrints:
    """"""

    def __init__(self):
        self._original_stdout = sys.stdout

    def __enter__(self):
        sys.stdout = open(os.devnull, "w", encoding=UTF_8)

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


with HiddenPrints():
    PYGAME = __import__("pygame")


draw = PYGAME.draw
display = PYGAME.display
init = PYGAME.init
display = PYGAME.display
font = PYGAME.font
event = PYGAME.event
QUIT = PYGAME.QUIT
mouse = PYGAME.mouse
MOUSEBUTTONDOWN = PYGAME.MOUSEBUTTONDOWN
