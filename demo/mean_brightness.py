"""
Create a dict keyed by unicode characters of the mean brightness of.

those.

characters. Useful for creating ascii or unicode gradients for ascii art.
"""

import os
import shutil

FONT = "Noto-Sans-Mono-Regular"

FONT = "../celestine/data/cascadia_code_regular.otf"

# Grab a good sample of Unicode characters - Change the ranges to include whatever unicode characters you're interested in.
unicode_string = "".join(map(chr, range(0, 256)))

# unicode_string = "#"

WIDTH = 320
HEIGHT = 320
PATH = "font"

import PIL
from PIL import (
    ImageDraw,
    ImageFont,
)


def file_name(index):
    string = str(index)
    fill = string.zfill(4)
    join = os.path.join(PATH, fill)
    file = f"{join}.png"
    return file


def make_image(character):
    image = PIL.Image.new("L", (RIGHT - LEFT, BOTTOM - TOP), 0)
    draw = ImageDraw.Draw(image, "L")
    font = ImageFont.truetype(FONT, 216)
    pos = (32 - LEFT, 32 - TOP)
    color = 255
    draw.text(pos, character, fill=color, font=font)
    return image


def test_col(image):
    global LEFT
    global RIGHT
    data = list(image.getdata())

    left = None
    right = None

    for col in range(WIDTH):
        found = False
        for row in range(HEIGHT):
            index = row * WIDTH + col
            found |= data[index] > 16

        if found:
            if not left:
                left = col
            right = col

    if not left or not right:
        raise AttributeError

    LEFT = min(left, LEFT)
    RIGHT = max(right, RIGHT)


def test_row(image):
    global TOP
    global BOTTOM
    data = list(image.getdata())

    top = None
    bottom = None

    for row in range(HEIGHT):
        found = False
        for col in range(WIDTH):
            index = row * WIDTH + col
            found |= data[index] > 16

        if found:
            if not top:
                top = row
            bottom = row

    if not top or not bottom:
        raise AttributeError

    TOP = min(top, TOP)
    BOTTOM = max(bottom, BOTTOM)


def reset():
    """Remove the directory and rebuild it."""

    path = PATH
    if os.path.islink(path):
        raise RuntimeError

    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=False, onerror=None)

    os.mkdir(path)


########################

# First save pass.
LEFT = 0
RIGHT = WIDTH
TOP = 0
BOTTOM = HEIGHT

reset()
for index, character in enumerate(unicode_string):
    file = file_name(index)
    image = make_image(character)
    image.save(file)


# Find dimensions.
LEFT = WIDTH
RIGHT = 0
TOP = HEIGHT
BOTTOM = 0
replace = []
for index, character in enumerate(unicode_string):
    file = file_name(index)
    image = PIL.Image.open(file)
    try:
        test_row(image)
        test_col(image)
    except AttributeError:
        continue
    replace.append(character)

unicode_string = replace

LEFT += 0
RIGHT += 1
TOP += 0
BOTTOM += 1


# Second save pass.
NULL = PIL.Image.open("null.png")
reset()
for index, character in enumerate(unicode_string):
    file = file_name(index)
    image = make_image(character)
    test = PIL.ImageChops.difference(image, NULL)
    good = False
    for data in list(test.getdata()):
        if data >= 16:
            good = True
            break
    if good:
        image.save(file)
