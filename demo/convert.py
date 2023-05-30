"""
Create a dict keyed by unicode characters of the mean brightness of.

those.

characters. Useful for creating ascii or unicode gradients for ascii art.
"""

import os
import shutil

FONT = "Noto-Sans-Mono-Regular"

FONT = "../celestine/data/cascadia_code_regular.otf"

WIDTH = 320
HEIGHT = 320
PATH = "font"

import PIL
from PIL import (
    ImageDraw,
    ImageFont,
)


# Grab a good sample of Unicode characters - Change the ranges to include whatever unicode characters you're interested in.
# unicode_string = "".join(map(chr, range(0, 0x10000)))
unicode_string = "".join(map(chr, range(0x2800, 0x2900)))

unicode_string = "F"

image = PIL.Image.open("font/00000000.png")
#image.show()


WIDTH, HEIGHT = image.size
assert(WIDTH >= 2)
assert(HEIGHT >= 4)


length_x = WIDTH - 2
length_y = HEIGHT - 4

pixels = list(image.getdata())


def call(index_x, index_y):
    index = index_y * WIDTH + index_x
    test = pixels[index] >= 16
    text = "1" if test else "0"
    return text


for index in range(256):
    index_x = index % 2
    index_y = index // 2
    text = ""
    text += "1" if index & 0b00000001 else "0"
    text += "1" if index & 0b00001000 else "0"

    text += "1" if index & 0b00000010 else "0"
    text += "1" if index & 0b00010000 else "0"

    text += "1" if index & 0b00000100 else "0"
    text += "1" if index & 0b00100000 else "0"

    text += "1" if index & 0b01000000 else "0"
    text += "1" if index & 0b10000000 else "0"

    count = index + 0x2800
    number = hex(count)
    split = number[2:]
    upper = split.upper()
    fill = upper.zfill(4)

    print(f"0b{text} : chr(0x{fill}),")


for index_y in range(0, HEIGHT - 4, 4):
    for index_x in range(0, WIDTH - 2, 2):
        text = ""
        text += call(index_x + 0, index_y + 0)
        text += call(index_x + 1, index_y + 0)
        text += call(index_x + 0, index_y + 1)
        text += call(index_x + 1, index_y + 1)
        text += call(index_x + 0, index_y + 2)
        text += call(index_x + 1, index_y + 2)
        text += call(index_x + 0, index_y + 3)
        text += call(index_x + 1, index_y + 3)
        #print(f"0b{text}")

for index in range(0x2800, 0x2900):
    number = hex(index)
    split = number[2:]
    upper = split.upper()
    #print(f"{index}:chr(0x{upper})")


# image is top to bottom, left to right

