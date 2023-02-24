""""""

# import pygame
import sys
import os

pygame = None


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


with HiddenPrints():
    pygame = __import__("pygame")


draw = pygame.draw
display = pygame.display
init = pygame.init
display = pygame.display
font = pygame.font
event = pygame.event
QUIT = pygame.QUIT
mouse = pygame.mouse
MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN
