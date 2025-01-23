""""""

import colorsys

import PIL
import PIL.Image


colours = []

choices = [index * 256 / 7 for index in range(8)]
crayola = []


limit = 8

red = []
green = []
blue = []
cyan = []
magenta = []
yellow = []
grey = []

counter = 0
for rr in range(limit):
    for gg in range(limit):
        for bb in range(limit):
            counter += 1
            pixel = (rr, gg, bb)
            big = max(rr, gg, bb)
            low = min(rr, gg, bb)

            if rr == gg and gg == bb:
                grey.append(pixel)
                continue

            if rr == gg:
                if bb > rr:
                    blue.append(pixel)
                else:
                    yellow.append(pixel)
                continue

            if gg == bb:
                if rr > gg:
                    red.append(pixel)
                else:
                    cyan.append(pixel)
                continue

            if bb == rr:
                if gg > bb:
                    green.append(pixel)
                else:
                    magenta.append(pixel)
                continue

            def findit(aa, oo, cc):

                sorter = [rr, gg, bb]
                sorter.sort()
                small = sorter[0]
                big = sorter[1]
                isitus = sorter[2]
                if aa != isitus:
                    return
                first = aa - big
                second = big - small
                if first > second:
                    oo.append(pixel)
                if first < second:
                    cc.append(pixel)
                if first == second:
                    total = rr + gg + bb + 3
                    compore = limit + limit + limit
                    if total + total > compore:
                        cc.append(pixel)
                    else:
                        oo.append(pixel)

            findit(rr, red, cyan)
            findit(gg, green, magenta)
            findit(bb, blue, yellow)


print(counter)
print(len(red))
print(len(green))
print(len(blue))
print(len(magenta))
print(len(yellow))
print(len(cyan))
print(len(grey))

grouphug = []
grouphug.extend(red)
grouphug.extend(green)
grouphug.extend(blue)
grouphug.extend(magenta)
grouphug.extend(yellow)
grouphug.extend(cyan)
grouphug.extend(grey)


length = len(grouphug) - 1
image = PIL.Image.new("RGB", (1024, 1024))
for y in range(1024):
    for x in range(1024):
        xx = x // 4
        yy = min(xx, length)
        picker = grouphug[yy]
        colour = (
            round(choices[picker[0]]),
            round(choices[picker[1]]),
            round(choices[picker[2]]),
        )
        image.putpixel((x, y), colour)

image.show()
