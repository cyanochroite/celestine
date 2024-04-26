""""""

import importlib
import os
import sys

import PIL
from PIL import Image

path = os.path.dirname(sys.path[0])
sys.path.insert(0, path)

celestine = importlib.import_module("celestine")
# celestine.main(sys.argv[1:], True)


color = "E0E0E0"

pre = '''<td class="td" style="background:#'''
post = '''" onmouseover="this.className='hov'; SetColor('#'''
final = """')" onmouseout="this.className='td'">&nbsp;</td>"""


def make(number):
    return format(number * 17, "02x").upper()


def hax(number):
    return format(number, "02x").upper()


def toop(x, y, z):
    return (x * 17, y * 17, z * 17)


def rainbow(color):
    x, y, z = color
    x = int(x, 16)
    y = int(y, 16)
    z = int(z, 16)
    return x, y, z


reds = []
greens = []
blues = []

with open("./text.txt", mode="rt") as file:
    for line in file:
        item = line.strip()
        red = item[0:2]
        green = item[2:4]
        blue = item[4:6]
        color = (red, green, blue)
        if green == blue:
            greens.append(color)
        if red == blue:
            reds.append(color)
        if red == green:
            blues.append(color)


def draw(name, colors):
    for color in colors:
        x, y, z = color
        r, g, b = rainbow(color)
        image = PIL.Image.new("RGB", (1024, 1024), color=(r, g, b))
        image.save(f"./test/{name}_{x}{y}{z}.png")


draw("magenta", reds)
draw("blue", blues)
draw("cyan", greens)
