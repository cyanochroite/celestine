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


def toop(x, y, z):
    return (x * 17, y * 17, z * 17)


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

print(reds)
print(greens)
print(blues)

print('<table class="table1"><tbody><tr>')
for z in range(1):
    for x in range(16):
        for y in range(16):
            xx = make(x)
            yy = make(y)
            zz = make(z)
            color = f"{xx}{yy}{zz}"
            color = f"{xx}{yy}{xx}"
            row = f"{pre}{color}{post}{color}{final}"
            print(row)
            # image = PIL.Image.new("RGB", (1024, 1024), color=toop(x, y, z))
            image = PIL.Image.new("RGB", (1024, 1024), color=toop(x, y, x))
            image.save(f"./test/{color}.png")
        print('</tr><tr>')
print('</tr></tbody></table>')


