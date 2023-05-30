"""
Create a dict keyed by unicode characters of the mean brightness of those
characters. Useful for creating ascii or unicode gradients for ascii art.
"""
from itertools import chain
import json
import subprocess

FONT = "Noto-Sans-Mono-Regular"

FONT = "../celestine/data/cascadia_code_regular.otf"

# Grab a good sample of Unicode characters - Change the ranges to include whatever unicode characters you're interested in.
unicode_string = "".join(map(chr, chain(range(32,127), range(162,191))))

unicode_string = "#"

WIDTH = 320
HEIGHT = 320

import PIL
from PIL import Image, ImageFont, ImageDraw



def file_name(index):
    string = str(index)
    fill = string.zfill(4)
    file = f"{fill}.png"
    return file


def save_image(text, file):
    image = PIL.Image.new("L", (RIGHT - LEFT, BOTTOM - TOP), 0)
    draw = ImageDraw.Draw(image, "L")
    font = ImageFont.truetype(FONT, 216)
    pos = (32 - LEFT, 32 - TOP)
    color = 255
    draw.text(pos, text, fill=color, font=font)
    image.save(file)



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
            found |= data[index] >= 128

        if found:
            if not left:
                left = col
            right = col

    if left:
        LEFT = min (left, LEFT)
    if right:
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
            found |= data[index] >= 128

        if found:
            if not top:
                top = row
            bottom = row

    if top:
        TOP = min (top, TOP)
    if bottom:
        BOTTOM = max(bottom, BOTTOM)

########################

# First save pass.
LEFT = 0
RIGHT = WIDTH
TOP = 0
BOTTOM = HEIGHT

for index, character in enumerate(unicode_string):
    file = file_name(index)
    save_image(character, file)




# Find dimensions.
LEFT = 0
RIGHT = WIDTH
TOP = HEIGHT
BOTTOM = 0
for index, character in enumerate(unicode_string):
    file = file_name(index)
    image = PIL.Image.open(file)
    test_row(image)
    test_col(image)

LEFT -= 3
RIGHT += 3
TOP -= 3
BOTTOM += 3


# Second save pass.
for index, character in enumerate(unicode_string):
    file = file_name(index)
    save_image(character, file)


print(TOP, BOTTOM)
print(LEFT, RIGHT)
print(RIGHT - LEFT, BOTTOM - TOP)


# Measure the mean brightness of each character in the png and save as a dict.
mean_brightness = { }



with open("meanbrightness.json", "w") as f:
    json.dump(mean_brightness, f)