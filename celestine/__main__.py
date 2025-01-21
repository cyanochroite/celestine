""""""

import colorsys
import math

import PIL
import PIL.Image

type F = float
type Z = int
type TZ3 = (int, int, int)

image = PIL.Image.new("L", (16, 16))
image.putpixel((0, 0), 30000000)


def hsv_to_rgb(hue: F, saturation: F, value: F) -> TZ3:
    """"""
    channels = colorsys.hsv_to_rgb(hue, saturation, value)

    def convert(channel: Z) -> Z:
        """"""
        color = channels[channel]
        number = color * 255
        result = round(number)
        return result

    red = convert(0)
    green = convert(1)
    blue = convert(2)
    result = (red, green, blue)
    return result


hues = [math.sqrt(index / 5) for index in range(1, 6)]
saturations = [index / 4 for index in range(1, 5)]

print(hues)
print(saturations)
hues = []
saturations = []

addit = 0
for hues in range(1, 5):
    hue = math.sqrt(hues) / 2

    for saturations in range(1, 5):
        saturation = saturations / 4

        colors = hues * 6
        for values in range(0, colors):
            addit += 1
            value = values / colors
            # print(hue, saturation, value)
            print(value, value * colors)


print(hues)
print(saturations)
print(addit)
